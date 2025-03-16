from fastapi import HTTPException
from sqlalchemy.orm import Session
import hashlib

from user_service_base.apis.default_api_base import BaseDefaultApi

from user_service_base.models.error_response import ErrorResponse
from user_service_base.models.user_profile_response import UserProfileResponse
from user_service_base.models.user_profile_update import UserProfileUpdate
from user_service_base.models.user_registration import UserRegistration
from user_service_base.models.v1_login_post200_response import V1LoginPost200Response
from user_service_base.models.v1_login_post_request import V1LoginPostRequest
from user_service_base.security_api import get_token_bearerAuth

from user_service_impl.models.users import User
from user_service_impl.database import SessionLocal

import user_service_impl.config as config


def hash_password(password: str) -> str:
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password


class ImplDefaultApi(BaseDefaultApi):
    async def v1_create_user_post(
        self,
        user_registration: UserRegistration,
    ) -> UserProfileResponse:
        """Регистрация пользователя по логину, паролю и электронной почте."""
        db = SessionLocal()
        user_exists = db.query(User).filter(
            (User.login == user_registration.login) | (
                User.email == user_registration.email)
        ).first()

        if user_exists:
            raise HTTPException(
                status_code=400, detail="Login or email already registered")

        db_user = User(
            login=user_registration.login,
            email=user_registration.email,
            password_hash=hash_password(user_registration.password),
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        response = UserProfileResponse(
            login=user_registration.login,
            email=user_registration.email,
            password=user_registration.password,
        )

        return response
