import time
import requests

def send_result(url: str, payload: dict):
    requests.post(url=url, json=payload)

def artificial_delay():
    time.sleep(10)