# pylint: disable= no-name-in-module

from typing import Dict, List, Literal, Union

from pydantic import AnyHttpUrl, BaseModel

JsonData = Union[Dict[str, object], List[Dict[str, object]]]


class ApiSource(BaseModel):
    name: str
    url: str
    method: Literal["GET", "POST"] = "GET"
    headers: Dict[str, str] = {}
    payload: JsonData = {}


class AsyncCalculationRequest(BaseModel):
    callback_url: AnyHttpUrl
    message: List[ApiSource]

    class Config:
        schema_extra = {
            "example": {
                "callback_url": "http://receiver:8001/test-me",
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
                        "name": "inception",
                        "url": "https://httpbin.org/post",
                        "payload": {"message": "It's me"},
                        "method": "POST",
                    },
                ],
            },
        }
