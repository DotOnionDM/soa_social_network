# coding: utf-8

from fastapi.testclient import TestClient


from endpoints.models.error_response import ErrorResponse  # noqa: F401
from endpoints.models.user_profile_response import UserProfileResponse  # noqa: F401
from endpoints.models.user_profile_update import UserProfileUpdate  # noqa: F401
from endpoints.models.user_registration import UserRegistration  # noqa: F401
from endpoints.models.v1_login_post200_response import V1LoginPost200Response  # noqa: F401
from endpoints.models.v1_login_post_request import V1LoginPostRequest  # noqa: F401


def test_v1_create_user_post(client: TestClient):
    """Test case for v1_create_user_post

    Регистрация нового пользователя
    """
    user_registration = {"password":"password","login":"login","email":"email"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/v1/createUser",
    #    headers=headers,
    #    json=user_registration,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_get_profile_get(client: TestClient):
    """Test case for v1_get_profile_get

    Получение данных профиля
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/getProfile",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_get_profile_put(client: TestClient):
    """Test case for v1_get_profile_put

    Обновление профиля после аутентификации
    """
    user_profile_update = {"first_name":"firstName","last_name":"lastName","phone_number":"phoneNumber","mail":"mail","birth_date":"2000-01-23","additional_attributes":{"key":"additionalAttributes"}}

    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PUT",
    #    "/v1/getProfile",
    #    headers=headers,
    #    json=user_profile_update,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_login_post(client: TestClient):
    """Test case for v1_login_post

    Аутентификация пользователя
    """
    v1_login_post_request = endpoints.V1LoginPostRequest()

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/v1/login",
    #    headers=headers,
    #    json=v1_login_post_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

