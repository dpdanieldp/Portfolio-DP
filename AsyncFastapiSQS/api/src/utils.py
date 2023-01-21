import logging
import traceback
import uuid
from typing import Union

import boto3
from fastapi import HTTPException

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def send_message_to_fifo_queue(
    msg: str,
    queue_name: str,
    message_group_id: str,
    message_deduplication_id: str = None,
) -> Union[str, HTTPException]:
    try:
        if message_deduplication_id is None:
            message_deduplication_id = str(uuid.uuid4())

        # Get the service resource
        sqs = boto3.resource("sqs")

        # Get the queue
        queue = sqs.get_queue_by_name(QueueName=queue_name)

        # Create a new message
        response = queue.send_message(
            MessageBody=msg,
            MessageGroupId=message_group_id,
            MessageDeduplicationId=message_deduplication_id,
        )
        # MessageGroupId is required for FIFO queues. You can't use it for Standard queues, look:
        # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.send_message
        # random MessageDeduplicationId is provided to avoid deduplication mechanism
        # in case of two or more requests with the same body within 5 mins, look:
        # https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagededuplicationid-property.html
        return response.get("MessageId", "None")
    except Exception as e:
        err_details = traceback.format_exc()
        error_msg = (
            f"❌ Sending message to queue: {queue_name} failed! Message: {msg}\n Error message: {e}."
            f" \n {err_details}"
        )
        logger.error(error_msg)
        raise HTTPException(500, "Request processing failed due to an internal error.")
