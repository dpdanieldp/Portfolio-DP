# pylint: disable= broad-except, invalid-name, missing-function-docstring, missing-module-docstring

import ast
import logging
import os
import time

import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def _calculate(calculation_request: dict, task_id: str):
    payload = {"results": [], "errors": [], "task_id": task_id}
    operations = {
        "+": (lambda num_1, num_2: num_1 + num_2),
        "-": (lambda num_1, num_2: num_1 - num_2),
        "*": (lambda num_1, num_2: num_1 * num_2),
        "/": (lambda num_1, num_2: num_1 / num_2),
    }
    response_timeout = int(os.getenv("RESPONSE_TIMEOUT", "60"))
    # artificial delay
    time.sleep(int(os.getenv("DELAY", "10")))

    for calc in calculation_request["message"]:
        func = operations[calc["operation"]]
        try:
            result = round(func(calc["num_1"], calc["num_2"]), calc["result_rounding"])
            payload["results"].append({calc["name"]: result})
        except Exception as e:
            payload["errors"].append({calc["name"]: str(e)})

    logger.info("Result for %s:  %s", task_id, payload)

    requests.post(url=calculation_request["callback_url"], json=payload, timeout=response_timeout)


def execute(event, _):
    logger.info("Received event: %s", event)

    message = event["Records"][0]
    msg_id = message.get("messageId")
    msg_body = ast.literal_eval(message.get("body", "{}"))

    logger.info("Processing: %s, message: %s", msg_id, msg_body)

    _calculate(calculation_request=msg_body, task_id=msg_id)
