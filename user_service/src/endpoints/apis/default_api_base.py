# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from endpoints.models.error_response import ErrorResponse
from endpoints.models.user_profile_response import UserProfileResponse
from endpoints.models.user_profile_update import UserProfileUpdate
from endpoints.models.user_registration import UserRegistration
from endpoints.models.v1_login_post200_response import V1LoginPost200Response
from endpoints.models.v1_login_post_request import V1LoginPostRequest
from endpoints.security_api import get_token_bearerAuth

class BaseDefaultApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDefaultApi.subclasses = BaseDefaultApi.subclasses + (cls,)
    async def v1_create_user_post(
        self,
        user_registration: UserRegistration,
    ) -> UserProfileResponse:
        """Регистрация пользователя по логину, паролю и электронной почте."""
        ...


    async def v1_get_profile_get(
        self,
    ) -> UserProfileResponse:
        """Получения профиля авторизованного пользователя."""
        ...


    async def v1_get_profile_put(
        self,
        user_profile_update: UserProfileUpdate,
    ) -> UserProfileResponse:
        """Изменение профиля пользователя после авторизации."""
        ...


    async def v1_login_post(
        self,
        v1_login_post_request: V1LoginPostRequest,
    ) -> V1LoginPost200Response:
        """Вход пользователя в систему по логину и паролю."""
        ...
