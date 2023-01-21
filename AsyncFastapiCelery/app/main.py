from fastapi import FastAPI
from src import routes
from starlette.requests import Request

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

app.include_router(routes.router)


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
