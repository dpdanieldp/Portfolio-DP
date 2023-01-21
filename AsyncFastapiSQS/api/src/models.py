# here are the universal models for many service functionalities
from typing import List

from pydantic import BaseModel


class UniversalAsyncResponse(BaseModel):
    results: List[dict]
    errors: List[dict]
    task_id: str


class AsyncInstantResponse(BaseModel):
    message: str
    task_id: str
    async_job_response_structure: UniversalAsyncResponse
