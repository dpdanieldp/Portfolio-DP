import json
import requests
from celery import shared_task

import settings
from src import utils



@shared_task
def retrieve_data_from_apis(data_request: dict):
    payload = {
        "results": [],
        "errors": []
    }
    utils.artificial_delay()
    for source in data_request["message"]:
        if source["method"] == "POST":
            try:
                response = perform_post_request(source)
                payload["results"].append({source["name"]: response})
            except Exception as e:
                payload["errors"].append({source["name"]: str(e)})
        else:
            try:
                response = perform_get_request(source)
                payload["results"].append({source["name"]: response})
            except Exception as e:
                payload["errors"].append({source["name"]: str(e)})
    utils.send_result(url=data_request["callback_url"], payload=payload)

def perform_post_request(request_details: dict) -> dict:
    response = requests.post(url=request_details["url"],
                             headers=request_details["headers"],
                             json=request_details["payload"],
                             timeout=300)
    response.raise_for_status()
    return response.json()

def perform_get_request(request_details: dict) -> dict:
    response = requests.get(url=request_details["url"],
                            headers=request_details["headers"],
                            timeout=300)

    response.raise_for_status()
    return response.json()

