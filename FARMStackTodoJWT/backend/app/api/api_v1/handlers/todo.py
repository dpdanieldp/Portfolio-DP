from typing import List
from uuid import UUID

from app.api.deps.user_deps import get_current_user
from app.models.user_model import User
from app.schemas.todo_schema import TodoCreate, TodoOut, TodoUpdate
from app.services.todo_service import TodoService
from fastapi import APIRouter, Security

todo_router = APIRouter()


@todo_router.get("/", summary="Get all todos of the user", response_model=List[TodoOut])
async def list_todos(current_user: User = Security(get_current_user, scopes=["todo:get_my"])):
    return await TodoService.list_user_todos(current_user)


@todo_router.post("/new", summary="Create Todo", response_model=TodoOut)
async def create_todo(
    data: TodoCreate,
    current_user: User = Security(get_current_user, scopes=["todo:create"]),
):
    return await TodoService.create_todo(current_user, data)


@todo_router.get("/{todo_id}", summary="Get a todo by todo_id", response_model=TodoOut)
async def retrieve_todo(
    todo_id: UUID,
    current_user: User = Security(get_current_user, scopes=["todo:get_my"]),
):
    return await TodoService.retrieve_todo(current_user, todo_id)


@todo_router.put("/{todo_id}", summary="Update todo by todo_id", response_model=TodoOut)
async def update_todo(
    todo_id: UUID,
    data: TodoUpdate,
    current_user: User = Security(get_current_user, scopes=["todo:update"]),
):
    return await TodoService.update_todo(current_user, todo_id, data)


@todo_router.delete("/{todo_id}", summary="Delete todo by todo_id")
async def delete_todo(
    todo_id: UUID,
    current_user: User = Security(get_current_user, scopes=["todo:delete"]),
):
    await TodoService.delete_todo(current_user, todo_id)
    return None
