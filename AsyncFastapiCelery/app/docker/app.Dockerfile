FROM python:3.9
WORKDIR /project
COPY ./requirements.txt /project/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /project/requirements.txt
COPY . /project/app
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
