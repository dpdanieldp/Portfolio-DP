from typing import List

from app.core import permissions
from decouple import config
from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    JWT_SECRET_KEY: str = config("JWT_SECRET_KEY", cast=str)
    JWT_REFRESH_SECRET_KEY: str = config("JWT_REFRESH_SECRET_KEY", cast=str)
    ALGORITHM: str = config("ALGORITHM", default="HS256", cast=str)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = config("ACCESS_TOKEN_EXPIRE_MINUTES", default=60, cast=int)
    REFRESH_TOKEN_EXPIRE_MINUTES: int = config(
        "REFRESH_TOKEN_EXPIRE_MINUTES", default=10080, cast=int
    )  # 7 days default
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:3000"]
    PROJECT_NAME: str = config("PROJECT_NAME", default="TODO LIST", cast=str)

    # Database
    MONGO_USERNAME: str = config("MONGO_USERNAME", cast=str)
    MONGO_PASSWORD: str = config("MONGO_PASSWORD", cast=str)
    MONGO_HOST: str = config("MONGO_HOST", cast=str)
    MONGO_PORT: str = config("MONGO_PORT", cast=str)
    MONGO_DB_NAME: str = config("MONGO_DB_NAME", default="test_one", cast=str)
    # Admin user
    ADMIN_EMAIL: str = config("ADMIN_EMAIL", cast=str)
    ADMIN_PASSWORD: str = config("ADMIN_PASSWORD", cast=str)
    # Permissions
    SCOPES_ALL: List[str] = list(permissions.SCOPES.keys())
    SCOPES_DEFAULT: List[str] = permissions.DEFAULT_SCOPES
    # feature flag- show admin endpoints in docs
    SHOW_ADMIN_DOCS: bool = config("SHOW_ADMIN_DOCS", default=False, cast=bool)

    class Config:
        case_sensitive = True


settings = Settings()
