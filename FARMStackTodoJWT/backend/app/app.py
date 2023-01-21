import pymongo
from app.api.api_v1.router import router
from app.core.config import settings
from app.models.todo_model import Todo
from app.models.user_model import User
from app.schemas.user_schema import AdminUserAuth
from app.services.user_service import UserService
from beanie import init_beanie
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.requests import Request

description = """
### This is example FastAPI app with JWT authentication and different authorisation levels for some endpoints 🚀
"""


app = FastAPI(
    title=settings.PROJECT_NAME,
    description=description,
    version="0.0.1",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    contact={
        "name": "Feel free to contact me on Linkedin",
        "url": "https://www.linkedin.com/in/daniel-pyrzanowski-77503b251",
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def app_init():
    """
    initialize crucial application services
    """

    db_client = AsyncIOMotorClient(
        f"mongodb://{settings.MONGO_USERNAME}:{settings.MONGO_PASSWORD}@" f"{settings.MONGO_HOST}:{settings.MONGO_PORT}"
    )[settings.MONGO_DB_NAME]

    await init_beanie(database=db_client, document_models=[User, Todo])
    admin_creation_log = await _create_admin_user()
    print(admin_creation_log)


app.include_router(router, prefix=settings.API_V1_STR)


async def _create_admin_user() -> str:
    admin = AdminUserAuth(
        email=settings.ADMIN_EMAIL,
        username="admin",
        password=settings.ADMIN_PASSWORD,
        scopes=settings.SCOPES_ALL,
    )
    try:
        admin_id = await UserService.create_admin(admin)
        return f"Admin user created: {admin_id}"
    except pymongo.errors.DuplicateKeyError:
        return "User with this email or username already exists, admin creation skipped"


@app.get("/", tags=["Welcome"])
def welcome(request: Request):
    return {
        "service_info": app.openapi().get("info", ""),
        "documentation_swagger": str(request.url) + "docs",
        "documentation_redoc": str(request.url) + "redoc",
    }


@app.get("/healthcheck", tags=["Healthcheck"])
def healthcheck():
    return {"state": "healthy"}
