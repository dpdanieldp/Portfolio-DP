# pylint: disable= no-name-in-module
# here are the universal models for many service functionalities
from typing import List

from pydantic import BaseModel


class UniversalAsyncResponse(BaseModel):
    results: List[dict]
    errors: List[dict]


class AsyncInstantResponse(BaseModel):
    message: str
    async_job_response_structure: UniversalAsyncResponse = {
        "results": [{}],
        "errors": [{}],
    }
