from datetime import datetime
from typing import List, Literal, Optional
from uuid import UUID

from app.core.config import settings
from pydantic import BaseModel, EmailStr, Field

AVAILABLE_SCOPES = tuple(settings.SCOPES_ALL)
SCOPES = List[Literal[AVAILABLE_SCOPES]]


class UserAuth(BaseModel):
    email: EmailStr = Field(..., description="user email")
    username: str = Field(..., min_length=5, max_length=50, description="user username")
    password: str = Field(..., min_length=5, max_length=24, description="user password")


class AdminUserAuth(UserAuth):
    scopes: List[str] = Field(..., description="admin user scopes")


class UserOut(BaseModel):
    user_id: UUID
    username: str
    email: EmailStr
    first_name: Optional[str]
    last_name: Optional[str]
    disabled: Optional[bool] = False


class AdminUserOut(UserOut):
    scopes: List[str]
    created_at: datetime
    updated_at: datetime


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class AdminUserUpdate(BaseModel):
    scopes: SCOPES
    disabled: Optional[bool] = None
