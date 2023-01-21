# pylint: disable= broad-except

from celery_worker import celery_app
from src import utils


@celery_app.task
def calculate(calculation_request: dict):
    payload = {"results": [], "errors": []}
    operations = {
        "+": (lambda num_1, num_2: num_1 + num_2),
        "-": (lambda num_1, num_2: num_1 - num_2),
        "*": (lambda num_1, num_2: num_1 * num_2),
        "/": (lambda num_1, num_2: num_1 / num_2),
    }
    utils.artificial_delay()
    for calc in calculation_request["message"]:
        func = operations[calc["operation"]]
        try:
            result = round(func(calc["num_1"], calc["num_2"]), calc["result_rounding"])
            payload["results"].append({calc["name"]: result})
        except Exception as e:
            payload["errors"].append({calc["name"]: str(e)})
    utils.send_result(url=calculation_request["callback_url"], payload=payload)
