import uvicorn
from fastapi import FastAPI
from mangum import Mangum
from src import routes, utils
from starlette.requests import Request

description = """
### This is example async FastAPI HTTP API 🚀
meant to be deployed on AWS as simple lambda and performs async tasks using SQS queues to communicate with workers
 (which are also lambda functions)
"""


app = FastAPI(
    title="Universal Async Service with AWS SQS",
    description=description,
    version="0.0.1",
    contact={
        "name": "Feel free to contact me on Linkedin",
        "url": "https://www.linkedin.com/in/daniel-pyrzanowski-77503b251",
    },
)

app.include_router(routes.router)

handler = Mangum(app)


@app.get("/", tags=["Welcome"])
def welcome(request: Request):
    utils.logger.info("endpoint: welcome")
    return {
        "service_info": app.openapi().get("info", ""),
        "documentation_swagger": str(request.url) + "docs",
        "documentation_redoc": str(request.url) + "redoc",
    }


@app.get("/healthcheck", tags=["Healthcheck"])
def healthcheck():
    utils.logger.info("endpoint: healthcheck")
    return {"state": "healthy"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=True,
    )
