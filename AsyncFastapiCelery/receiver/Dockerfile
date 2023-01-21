FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt
EXPOSE 8001
CMD ["uvicorn", "receiver:app", "--host", "0.0.0.0", "--port", "8001"]
