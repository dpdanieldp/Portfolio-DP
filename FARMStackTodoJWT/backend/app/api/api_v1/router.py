from app.api.api_v1.handlers import admin, todo, user
from app.api.auth.jwt import auth_router
from app.core.config import settings
from fastapi import APIRouter

router = APIRouter()

router.include_router(user.user_router, prefix="/user", tags=["Users"])
router.include_router(todo.todo_router, prefix="/todo", tags=["Todo"])
router.include_router(auth_router, prefix="/auth", tags=["Auth"])
router.include_router(
    admin.admin_router,
    prefix="/admin",
    tags=["Admin"],
    include_in_schema=settings.SHOW_ADMIN_DOCS,
)
