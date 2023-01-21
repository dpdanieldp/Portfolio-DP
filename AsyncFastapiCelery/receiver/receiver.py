import json

from fastapi import Body, FastAPI
from starlette.requests import Request

description = """
### This is example tasks results receiver for async FastAPI HTTP API 🚀
"""


app = FastAPI(
    title="Receiver",
    description=description,
    version="0.0.1",
    contact={
        "name": "Feel free to contact me on Linkedin",
        "url": "https://www.linkedin.com/in/daniel-pyrzanowski-77503b251",
    },
)


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


@app.post("/test-me", tags=["Test me"])
async def print_payload(payload: dict = Body(...)):
    """
    This is example endpoint for testing async work of the service-
    you can pass this endpoint as callback_url making requests
    to Async Tasks endpoints to print result payload from asynchronous jobs
    """
    print("-" * 20)
    print(json.dumps(payload, indent=2))
    return payload
