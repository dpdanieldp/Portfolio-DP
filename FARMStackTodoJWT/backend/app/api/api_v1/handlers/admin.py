# define endpoints available only for admin here

from typing import Dict, List
from uuid import UUID

import pymongo
from app.api.deps.user_deps import get_current_user
from app.core.permissions import SCOPES
from app.models.user_model import User
from app.schemas.todo_schema import AdminTodoOut
from app.schemas.user_schema import AdminUserOut, AdminUserUpdate
from app.services.todo_service import TodoService
from app.services.user_service import UserService
from fastapi import APIRouter, HTTPException, Security, status

admin_router = APIRouter()

users_path = "/users"
todos_path = "/todos"


# actions related to users
@admin_router.get(
    users_path + "/",
    summary="Get details of all users",
    response_model=List[AdminUserOut],
)
async def get_all_users(_: User = Security(get_current_user, scopes=["admin"])):
    return await UserService.get_all_users()


@admin_router.put(users_path + "/{user_id}", summary="Update User", response_model=AdminUserOut)
async def update_user(
    user_id: UUID,
    data: AdminUserUpdate,
    _: User = Security(get_current_user, scopes=["admin"]),
):
    try:
        return await UserService.update_user(user_id, data)
    except pymongo.errors.OperationFailure:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User does not exist")


# actions related to todos
@admin_router.get(
    todos_path + "/",
    summary="Get all todos of all user",
    response_model=List[AdminTodoOut],
)
async def list_todos(_: User = Security(get_current_user, scopes=["admin"])):
    return await TodoService.list_all_todos()


# actions related to permissions
@admin_router.get("/permissions", summary="Get permissions description", response_model=Dict[str, str])
def get_permissions_description(_: User = Security(get_current_user, scopes=["admin"])):
    return SCOPES
