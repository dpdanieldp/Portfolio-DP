import os

SLACK_CHANNEL = os.getenv("SLACK_CHANNEL", "general")
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
#
RESPONSE_TIMEOUT = int(os.getenv("RESPONSE_TIMEOUT", "20"))
