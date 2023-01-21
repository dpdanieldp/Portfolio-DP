import settings
from fastapi import APIRouter
from src import models, utils
from src.data import data_models

router = APIRouter(prefix="/v1/data")


@router.post(
    path="/from-api",
    summary="Retrieve data from multiple REST API sources",
    response_model=models.AsyncInstantResponse,
)
def retrieve_data_from_apis(
    request: data_models.AsyncCalculationRequest,
):
    """
    You can retrieve data from multiple APIs at once.

    APIs have to return JSON response.

    You have to provide `name` for source and API `url`, it is also possible to specify `headers` and `payload`
     and to select the request `method` (default: GET)
    """
    queue_name = settings.DATA_Q_NAME
    msg = str(request.dict())
    task_id = utils.send_message_to_fifo_queue(msg=msg, queue_name=queue_name, message_group_id="data")
    utils.logger.info(
        f"endpoint: retrieve_data_from_apis, queue_name: {queue_name}, message: {msg}," f" task_id: {task_id}"
    )
    return models.AsyncInstantResponse(
        message="Processing of your request has started",
        task_id=task_id,
        async_job_response_structure={
            "results": [{}],
            "errors": [{}],
            "task_id": task_id,
        },
    )
