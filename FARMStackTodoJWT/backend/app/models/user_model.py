from datetime import datetime
from typing import List, Optional
from uuid import UUID, uuid4

from app.core.config import settings
from beanie import Document, Indexed, Replace, Update, after_event
from pydantic import EmailStr, Field


class User(Document):
    user_id: UUID = Field(default_factory=uuid4)
    username: Indexed(str, unique=True)
    email: Indexed(EmailStr, unique=True)
    hashed_password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    disabled: Optional[bool] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    #
    scopes: List[str] = Field(default=settings.SCOPES_DEFAULT)

    def __repr__(self) -> str:
        return f"<User {self.email}>"

    def __str__(self) -> str:
        return self.email

    def __hash__(self) -> int:
        return hash(self.email)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, User):
            return self.email == other.email
        return False

    @property
    def create(self) -> datetime:
        return self.id.generation_time


    @after_event(Replace, Update)
    def update_update_at(self):
        self.updated_at = datetime.utcnow()

    class Settings:
        name = "users"
