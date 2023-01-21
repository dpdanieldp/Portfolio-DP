import time

import requests
import settings


def send_result(url: str, payload: dict):
    requests.post(url=url, json=payload, timeout=60)


def artificial_delay():
    time.sleep(int(settings.DELAY))
