import settings
from fastapi import APIRouter
from src import models, utils
from src.calculation import calc_models

router = APIRouter(prefix="/v1/calculation")


@router.post(
    path="/basic",
    summary="Perform basic calculations",
    response_model=models.AsyncInstantResponse,
)
def calculate_basic(
    request: calc_models.AsyncCalculationRequest,
):
    """
    Perform addition, subtraction, multiplication and division on any number of pairs of numbers.
    You can specify the rounding of the result.
    """
    queue_name = settings.CALC_Q_NAME
    msg = str(request.dict())
    task_id = utils.send_message_to_fifo_queue(msg=msg, queue_name=queue_name, message_group_id="calculation")
    utils.logger.info(f"endpoint: calculate_basic, queue_name: {queue_name}, message: {msg}, task_id: {task_id}")
    return models.AsyncInstantResponse(
        message="Processing of your request has started",
        task_id=task_id,
        async_job_response_structure={
            "results": [{}],
            "errors": [{}],
            "task_id": task_id,
        },
    )
