import pymongo
from app.api.deps.user_deps import get_current_user
from app.models.user_model import User
from app.schemas.user_schema import UserAuth, UserOut, UserUpdate
from app.services.user_service import UserService
from fastapi import APIRouter, Depends, HTTPException, status

user_router = APIRouter()


@user_router.post("/new", summary="Create new user", response_model=UserOut)
async def create_user(data: UserAuth):
    try:
        return await UserService.create_user(data)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email or username already exists",
        )


@user_router.get("/me", summary="Get details of currently logged in user", response_model=UserOut)
async def get_me(user: User = Depends(get_current_user)):
    return user


@user_router.put("/me", summary="Update current User", response_model=UserOut)
async def update_user(data: UserUpdate, user: User = Depends(get_current_user)):
    try:
        return await UserService.update_user(user.user_id, data)
    except pymongo.errors.OperationFailure:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User does not exist")
