from typing import List, Dict, Any, Union, Literal

from pydantic import BaseModel, AnyHttpUrl

class Calculation(BaseModel):
    name: str
    num_1: float
    num_2: float
    operation: Literal["+","-","*","/"]
    result_rounding: int


class AsyncCalculationRequest(BaseModel):
    callback_url: AnyHttpUrl
    message: List[Calculation]

    class Config:
        schema_extra = {
            "example": {
                "callback_url": "http://127.0.0.1:8000/test-me",
                "message": [
                    {"name": "calc_0", "num_1": 123, "num_2": 0.75647, "operation": "+", "result_rounding": 2},
                    {"name": "calc_1", "num_1": 785687256, "num_2": 0.75647, "operation": "-", "result_rounding": 4},
                    {"name": "calc_2", "num_1": 0.877666663555222222, "num_2": 1000, "operation": "*", "result_rounding": -1},
                    {"name": "calc_3", "num_1": 1, "num_2": 0, "operation": "/", "result_rounding": 7},
                ],
            },
        }


