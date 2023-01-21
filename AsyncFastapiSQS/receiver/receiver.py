import ast
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def receive_request(event, *_):
    body = event.get("body")
    logger.info(body)
    return {"message": ast.literal_eval(body)}
