# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from user_service_base.apis.default_api_base import BaseDefaultApi
import user_service_impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from user_service_base.models.extra_models import TokenModel  # noqa: F401
from user_service_base.models.error_response import ErrorResponse
from user_service_base.models.user_profile_response import UserProfileResponse
from user_service_base.models.user_profile_update import UserProfileUpdate
from user_service_base.models.user_registration import UserRegistration
from user_service_base.models.v1_login_post200_response import V1LoginPost200Response
from user_service_base.models.v1_login_post_request import V1LoginPostRequest
from user_service_base.security_api import get_token_bearerAuth

router = APIRouter()

ns_pkg = user_service_impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/v1/createUser",
    responses={
        201: {"model": UserProfileResponse, "description": "Пользователь успешно зарегистрирован"},
        400: {"model": ErrorResponse, "description": "Ошибка валидации входящих данных"},
    },
    tags=["default"],
    summary="Регистрация нового пользователя",
    response_model_by_alias=True,
)
async def v1_create_user_post(
    user_registration: UserRegistration = Body(None, description=""),
) -> UserProfileResponse:
    """Регистрация пользователя по логину, паролю и электронной почте."""
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().v1_create_user_post(user_registration)


@router.post(
    "/v1/login",
    responses={
        200: {"model": V1LoginPost200Response, "description": "Успешная авторизация"},
        401: {"model": ErrorResponse, "description": "Неверный логин или пароль"},
    },
    tags=["default"],
    summary="Аутентификация пользователя",
    response_model_by_alias=True,
)
async def v1_login_post(
    v1_login_post_request: V1LoginPostRequest = Body(None, description=""),
) -> V1LoginPost200Response:
    """Вход пользователя в систему по логину и паролю."""
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().v1_login_post(v1_login_post_request)


@router.get(
    "/v1/profile",
    responses={
        200: {"model": UserProfileResponse, "description": "Успешное получение данных профиля"},
        401: {"model": ErrorResponse, "description": "Ошибка авторизации"},
    },
    tags=["default"],
    summary="Получение данных профиля",
    response_model_by_alias=True,
)
async def v1_profile_get(
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> UserProfileResponse:
    """Получения профиля авторизованного пользователя."""
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().v1_profile_get()


@router.put(
    "/v1/profile",
    responses={
        200: {"model": UserProfileResponse, "description": "Профиль успешно обновлен"},
        400: {"model": ErrorResponse, "description": "Ошибка в данных, присланных для обновления"},
        401: {"model": ErrorResponse, "description": "Ошибка авторизации"},
    },
    tags=["default"],
    summary="Обновление профиля после аутентификации",
    response_model_by_alias=True,
)
async def v1_profile_put(
    user_profile_update: UserProfileUpdate = Body(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> UserProfileResponse:
    """Изменение профиля пользователя после авторизации."""
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().v1_profile_put(user_profile_update)
