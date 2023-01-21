from typing import List, Literal
from uuid import UUID

from app.core.config import settings
from pydantic import BaseModel

AVAILABLE_SCOPES = tuple(settings.SCOPES_ALL)
SCOPES = List[Literal[AVAILABLE_SCOPES]]


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str


class TokenPayload(BaseModel):
    sub: UUID = None
    exp: int = None
