import uvicorn
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
from celery import Celery

from src import routes
import settings

description = """
### This is example async FastAPI HTTP API 🚀
"""


app = FastAPI(
    title="Universal Async Service",
    description=description,
    version="0.0.1",
    contact={
        "name": "Feel free to contact me on Linkedin",
        "url": "https://www.linkedin.com/in/daniel-pyrzanowski-77503b251",
    },
)

# origins = [
#     "http://localhost:3000",
#     "http://127.0.0.1:3000",
# ]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


app.include_router(routes.router)


celery = Celery(
    __name__,
    broker=f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.REDIS_DB}",
    backend=f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.REDIS_DB}",
)
celery.conf.imports = [
    "src.calculation.tasks",
    "src.data.tasks",
]



@app.get("/", tags=["Welcome"])
def welcome(request: Request):
    return {
        "Servis info": app.openapi().get("info", ""),
        "documentation_swagger": str(request.url) + "docs",
        "documentation_redoc": str(request.url) + "redoc",
    }


@app.get("/healthcheck", tags=["Healthcheck"])
def healthcheck():
    return {"state": "healthy"}


@app.post('/test-me', tags=["Test me"])
async def print_payload(
        payload: dict = Body(...)
):
    """
    This is example enpoint for testing async work of the service-
    you can pass this endpoint as callback_url making requests
    to Async Tasks endpoints to print result payload from asynchronous jobs
    """
    print("-"*20)
    print(payload)
    return payload


# for testing
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=True,
    )
