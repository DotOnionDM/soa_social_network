# coding: utf-8

"""
    User Service API

    API для сервиса пользователей.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from fastapi import FastAPI

from endpoints.apis.default_api import router as DefaultApiRouter

app = FastAPI(
    title="User Service API",
    description="API для сервиса пользователей.",
    version="1.0.0",
)

app.include_router(DefaultApiRouter)
