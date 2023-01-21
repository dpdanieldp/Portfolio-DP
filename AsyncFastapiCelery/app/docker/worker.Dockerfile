FROM python:3.9
WORKDIR /project
COPY ./requirements.txt /project/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /project/requirements.txt
COPY . /project/app
CMD ["celery", "-A", "app.celery_worker.celery_app", "worker", "--loglevel=info"]
