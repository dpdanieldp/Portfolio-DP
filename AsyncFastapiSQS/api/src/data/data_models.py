from typing import Dict, List, Literal, Union

import settings
from pydantic import BaseModel

JsonData = Union[Dict[str, object], List[Dict[str, object]]]


class ApiSource(BaseModel):
    name: str
    url: str
    method: Literal["GET", "POST"] = "GET"
    headers: Dict[str, str] = {}
    payload: JsonData = {}


class AsyncCalculationRequest(BaseModel):
    callback_url: str
    message: List[ApiSource]

    class Config:
        schema_extra = {
            "example": {
                "callback_url": settings.EXAMPLE_RECEIVER_URL,
                "message": [
                    {
                        "name": "cat_fact",
                        "url": "https://catfact.ninja/fact",
                        "method": "GET",
                    },
                    {
                        "name": "random_joke",
                        "url": "https://official-joke-api.appspot.com/random_joke",
                    },
                    {
                        "name": "dog_image",
                        "url": "https://dog.ceo/api/breeds/image/random",
                    },
                    {
                        "name": "post_request",
                        "url": "https://httpbin.org/post",
                        "payload": {"message": "It's me"},
                        "method": "POST",
                    },
                ],
            },
        }
