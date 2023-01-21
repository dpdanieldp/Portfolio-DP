
FROM python:3.9
WORKDIR /app
COPY ./rest_api_game /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt
CMD ["python", "app.py"]