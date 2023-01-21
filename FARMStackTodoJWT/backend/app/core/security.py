from datetime import datetime, timedelta
from typing import Any, Literal, Union

from app.core.config import settings
from jose import jwt
from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ACCESS = "access"
REFRESH = "refresh"


def create_token(
    token_type: Literal[ACCESS, REFRESH],
    subject: Union[str, Any],
    expires_delta: int = None,
) -> str:
    jwt_keys = {
        ACCESS: settings.JWT_SECRET_KEY,
        REFRESH: settings.JWT_REFRESH_SECRET_KEY,
    }
    jwt_expiration_times = {
        ACCESS: settings.ACCESS_TOKEN_EXPIRE_MINUTES,
        REFRESH: settings.REFRESH_TOKEN_EXPIRE_MINUTES,
    }

    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=jwt_expiration_times[token_type])

    to_encode = {"exp": expires_delta, "sub": str(subject)}  # , "scopes": scopes
    encoded_jwt = jwt.encode(to_encode, jwt_keys[token_type], settings.ALGORITHM)
    return encoded_jwt


def get_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)
