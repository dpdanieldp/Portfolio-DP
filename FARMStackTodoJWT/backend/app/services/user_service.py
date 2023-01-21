from typing import List, Optional
from uuid import UUID

import pymongo
from app.core.security import get_password, verify_password
from app.models.user_model import User
from app.schemas.user_schema import AdminUserAuth, UserAuth, UserUpdate


class UserService:
    @staticmethod
    async def create_user(user: UserAuth):
        user_in = User(
            username=user.username,
            email=user.email,
            hashed_password=get_password(user.password),
        )
        await user_in.save()
        return user_in

    @staticmethod
    async def create_admin(admin: AdminUserAuth):
        admin_in = User(
            username=admin.username,
            email=admin.email,
            hashed_password=get_password(admin.password),
            scopes=admin.scopes,
        )
        await admin_in.save()
        return admin_in

    @staticmethod
    async def authenticate(email: str, password: str) -> Optional[User]:
        user = await UserService.get_user_by_email(email=email)
        if not user:
            return None
        if not verify_password(password=password, hashed_pass=user.hashed_password):
            return None

        return user

    @staticmethod
    async def get_user_by_email(email: str) -> Optional[User]:
        user = await User.find_one(User.email == email)
        return user

    @staticmethod
    async def get_user_by_id(id: UUID) -> Optional[User]:
        user = await User.find_one(User.user_id == id)
        return user

    @staticmethod
    async def get_all_users() -> List[User]:
        users = await User.find().to_list()
        return users

    @staticmethod
    async def update_user(id: UUID, data: UserUpdate) -> User:
        user = await User.find_one(User.user_id == id)
        if not user:
            raise pymongo.errors.OperationFailure("User not found")

        await user.update({"$set": data.dict(exclude_unset=True)})
        return user
