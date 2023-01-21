from typing import Any

from app.api.deps.user_deps import get_current_user
from app.core.config import settings
from app.core.security import ACCESS, REFRESH, create_token
from app.models.user_model import User
from app.schemas.auth_schema import TokenPayload, TokenSchema
from app.schemas.user_schema import UserOut
from app.services.user_service import UserService
from fastapi import APIRouter, Body, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from pydantic import ValidationError

auth_router = APIRouter()


@auth_router.post(
    "/login",
    summary="Create access and refresh tokens for user",
    response_model=TokenSchema,
)
async def login(form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    # check by email
    user = await UserService.authenticate(email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password",
        )

    return {
        "access_token": create_token(token_type=ACCESS, subject=user.user_id),
        "refresh_token": create_token(token_type=REFRESH, subject=user.user_id),
    }


@auth_router.post("/test-token", summary="Test if the access token is valid", response_model=UserOut)
async def test_token(user: User = Depends(get_current_user)):
    return user


@auth_router.post("/refresh", summary="Refresh token", response_model=TokenSchema)
async def refresh_token(refresh_token: str = Body(...)):
    """
    Send your `refresh_token` in payload to get new `access_token` and `refresh_token`
    """
    try:
        payload = jwt.decode(
            refresh_token,
            settings.JWT_REFRESH_SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )
        token_data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = await UserService.get_user_by_id(token_data.sub)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid token for user",
        )
    return {
        "access_token": create_token(token_type=ACCESS, subject=user.user_id),
        "refresh_token": create_token(token_type=REFRESH, subject=user.user_id),
    }
