import os

from celery import Celery

celery_app = Celery(__name__)

# Redis
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = os.getenv("REDIS_PORT", "6379")
REDIS_DB = os.getenv("REDIS_DB", "0")

redis_url = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"

celery_app.conf.broker_url = redis_url
celery_app.conf.result_backend = redis_url

celery_app.conf.imports = [
    "src.calculation.tasks",
    "src.data.tasks",
]
