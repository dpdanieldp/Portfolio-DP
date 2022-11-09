from fastapi import APIRouter, Header

from src import utils, models
from src.data import data_models, tasks

router = APIRouter(prefix="/v1/data")


@router.post(
    path="/from-api",
    summary="Retrieve data from multiple REST API sources",
    response_model=models.AsyncInstantResponse,
)
async def retrieve_data_from_apis(
    request: data_models.AsyncCalculationRequest,
):
    """
    You can retrieve data from multiple APIs at once.

    APIs have to return JSON response.

    You have to provide `name` for source and API `url`, it is also possible to specify `headers` and `payload` and to select the request `method` (default: GET)
    """
    tasks.retrieve_data_from_apis.delay(request.dict())
    return models.AsyncInstantResponse(message="processing of your request has started")
