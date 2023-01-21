from fastapi import APIRouter
from src import models
from src.calculation import calc_models, tasks

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
    tasks.calculate.delay(request.dict())
    return models.AsyncInstantResponse(message="processing of your request has started")
