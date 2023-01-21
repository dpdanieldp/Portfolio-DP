# pylint: disable= broad-except, invalid-name, missing-function-docstring, missing-module-docstring
import ast
import logging
import os
import time

import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def _retrieve_data_from_apis(data_request: dict, task_id: str):
    payload = {"results": [], "errors": [], "task_id": task_id}
    response_timeout = int(os.getenv("RESPONSE_TIMEOUT", "20"))

    # artificial delay
    time.sleep(int(os.getenv("DELAY", "10")))

    for source in data_request["message"]:
        if source["method"] == "POST":
            try:
                response = _perform_post_request(source)
                payload["results"].append({source["name"]: response})
            except Exception as e:
                payload["errors"].append({source["name"]: str(e)})
        else:
            try:
                response = _perform_get_request(source)
                payload["results"].append({source["name"]: response})
            except Exception as e:
                payload["errors"].append({source["name"]: str(e)})
    logger.info("Result for %s:  %s", task_id, payload)
    requests.post(url=data_request["callback_url"], json=payload, timeout=response_timeout)


def _perform_post_request(request_details: dict, timeout: int = 10) -> dict:
    response = requests.post(
        url=request_details["url"],
        headers=request_details["headers"],
        json=request_details["payload"],
        timeout=timeout,
    )
    response.raise_for_status()
    return response.json()


def _perform_get_request(request_details: dict, timeout: int = 10) -> dict:
    response = requests.get(url=request_details["url"], headers=request_details["headers"], timeout=timeout)

    response.raise_for_status()
    return response.json()


def execute(event, _):
    logger.info("Received event: %s", event)
    # since the lambda is triggered by fifo queue, there is only one message in event
    # in case of error in this lambda the msg is passed to dlq and is handled by logger lambda
    message = event["Records"][0]
    msg_id = message.get("messageId")
    msg_body = ast.literal_eval(message.get("body", "{}"))

    logger.info("Processing: %s, message: %s", msg_id, msg_body)

    _retrieve_data_from_apis(data_request=msg_body, task_id=msg_id)
