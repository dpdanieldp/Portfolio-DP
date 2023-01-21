# pylint: disable= broad-except, invalid-name, missing-function-docstring, missing-module-docstring

import ast
import logging
import traceback

import requests
import settings
from slack_sdk import WebClient

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def _send_slack_msg(slack_client: WebClient, slack_channel: str, msg: str, msg_max_len: int = 3000):
    chunks = [msg[i : i + msg_max_len] for i in range(0, len(msg), msg_max_len)]
    for chunk in chunks:
        slack_client.chat_postMessage(channel="#" + slack_channel, text=chunk)


def _send_failure_msg_to_callback_url(callback_url: str, message: dict, task_id: str):
    msg = {"details": "task failed for unknown reason", "message": message}
    payload = {"results": [{}], "errors": [msg], "task_id": task_id}

    requests.post(url=callback_url, json=payload, timeout=settings.RESPONSE_TIMEOUT)


def execute(event, _):
    # event structure for fifo queue- look:
    # https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#example-standard-queue-message-event
    logger.info("Received event: %s", event)

    message = event["Records"][0]
    msg_id = message.get("messageId")
    msg_body = ast.literal_eval(message.get("body", "{}"))

    failed_task_msg = f"Message in Dead Letter Queue:\n task_id: {msg_id}," f"\n'body': {msg_body}"
    logger.info(failed_task_msg)

    _send_failure_msg_to_callback_url(
        callback_url=msg_body.get("callback_url"),
        message=msg_body,
        task_id=msg_id,
    )

    slack_token = settings.SLACK_BOT_TOKEN

    if slack_token:
        try:
            slack_client = WebClient(token=slack_token)
            _send_slack_msg(
                slack_client=slack_client,
                slack_channel=settings.SLACK_CHANNEL,
                msg=failed_task_msg,
            )
        except Exception as e:
            err_details = traceback.format_exc()
            error_msg = f"❌ Sending slack message failed! error message: {e}." f" \n {err_details}"
            logger.error(error_msg)
