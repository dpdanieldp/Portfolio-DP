# Async FastAPI Celery

## Overwiev

This is a webapp built with **FastAPI and Celery** offering API gateway in form of FastAPI REST API 
and is able to perform async tasks using celry workers

The service can perform two example tasks:
1. Basic calculation (addition, subtraction, multiplication and division) on any number of pairs of numbers
2. Fetching data from any number of REST APIs (which return a json response) using GET or POST request

These tasks are artificially delayed to demonstrate the asynchronous operation of the service and to mimic processes that are not immediate.


### How it works

1. Client sends POST request to API endpoint in which `callback_url` has to be passed to receive result of operation (`RECEIVER` has to be able to accept `POST` request)
    
    example request payload: 
    ```json
    {
      "callback_url": "https://qju5rcoarg6a4bpxjf3joj3x7y0cfyfk.lambda-url.eu-west-1.on.aws/",
      "message": [
        {
          "name": "calc_0",
          "num_1": 123,
          "num_2": 0.75647,
          "operation": "+",
          "result_rounding": 2
        },
        {
          "name": "calc_1",
          "num_1": 785687256,
          "num_2": 0.75647,
          "operation": "-",
          "result_rounding": 4
        }
      ]
    }
    ```
2. If request structure is correct, API calls proper celery task
(depending on request endpoint).
4. If request structure is not correct, the client get `[422] Error: Unprocessable Entity` response detailing the error in the request structure.

   If at this stage the message fails to be sent to the queue, the client gets `[500] internal error` response.

   If the message was successfully sent to the queue, the client receives a `[200]` response 
for its request with information about the structure of the response,
which will be passed to the `callback_url` after the task is completed:

     ```json
    {
    "message": "Processing of your request has started",
    "async_job_response_structure": {
    "results": [{}],
    "errors": [{}]
   }
   }
    ```
5. Message in queue triggers proper lambda function(worker) and is passed to it to perform task.
6. If the task is completed, the worker sends its result to the `callback_url` via `POST` request and the process is finished.
    
   example message after task completion: 
    ```json
    {
   "results": [
   {
   "calc_0": 123.76
   },
    {
   "calc_1": 785687255.2435
   }
   ],
   "errors": [
   
   ]
   }
    ```
  

### Project structure
`app` directory contains code of the service,

Using [FastAPI](https://fastapi.tiangolo.com/) to build a REST API, we can easily define the required request structure for each endpoint,
gain automatic request validation, descriptive errors in case of inconsistencies,
and automatically created swagger and redoc documentation.

`receiver` directory contains example code of very simple webapp with url which can be run locally and used as `RECEIVER` with `callback_url`

`manifests` directory contains `.yaml` files describing **k8s** objects.

### How to try it out
The project is prepared to be run locally in docker using **docker-compose** as well as in **kubernetes** cluster.
1. Change name of `AsyncFastapiCelery/.env.example` file to `.env`
2. Install, setup and run [Docker Desktop](https://www.docker.com/)
3. Open Terminal and `cd` to `AsyncFastapiCelery`
####Run in docker:
4. run `make up` -this command will build and run Docker containers for:
   1. Webapp - on http://localhost:8000
   2. Example receiver - on http://localhost:8001
   3. Redis
   4. Celery worker
   5. [Flower](https://flower.readthedocs.io/en/latest/) - on http://localhost:5555 (**login**: example_user, **password**: example_password)
5. Go to http://localhost:8000/docs and try the service using Swagger UI by clicking `Try it out` button in any of two `POST` endpoints- you will see immediate API response in the Swagger UI and after a while you will also see full task result sent to RECEIVER printed out in your Terminal where docker-compose prints logs.
6. To stop all containers press `Ctrl+C` in the Terminal
####Run locally in kubernetes using minikube:
4. [Install minikube](https://minikube.sigs.k8s.io/docs/start/) 
5. Start minikube:
```bash
$ minikube start
```
6. Build docker images:
```bash
$ docker-compose build
```
7. Push docker images:
```bash
$ docker-compose push
```
8. Apply kubernetes manifest files:
```bash
$ kubectl apply -f manifests/
```
9. Access applications running within minikube: 

   In new terminal window (it will ask for a password):
```bash
$ minikube tunnel
```
10. Go to http://localhost:80/docs and try the service using Swagger UI by clicking `Try it out` button in any of two `POST` endpoints. You can monitor messages passed to celery workers using Flower on http://localhost:5555 (**login**: example_user, **password**: example_pass)

Please note: RECEIVER is not part of k8s deployment so to get final task result you have to provide `callback_url` to separately deployed receiver (you can use example receiver from: `AsyncFastapiSQS/receiver`)

<hr>

Thanks for your visit, feel free to contact me on [LinkedIn](https://www.linkedin.com/in/daniel-pyrzanowski-77503b251)