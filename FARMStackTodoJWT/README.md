# FARM Stack Todo JWT

`FARMStackTodoJWT` is a full stack todo application built with FARM stack.
FastAPI and MongoDB on the backend and ReactJS on the frontend.

`JWT authentication` is implemented in the service, as well as different levels of authorization required to perform certain actions.

The API also has endpoints configured for an admin user with all permissions (the admin user is created automatically when the application is launched using credentials passed in env variables - defined in the  `FARMStackTodoJWT/backend/app/.env.example`)

Every new user gets default permissions (can be found in `FARMStackTodoJWT/backend/app/core/permissions.py`). User permissions can be updated by admin user using admin endpoint. 

Visibility of admin endpoint in Swagger and Redoc docs can be changed using env feature flag `SHOW_ADMIN_DOCS`.

<hr>

## How to try it out

The project is prepared to be run locally in docker using docker-compose.

1. Install, setup and run [Docker Desktop](https://www.docker.com/)
2. Open Terminal and `cd` to `FARMStackTodoJWT`
3. run `make up` -this command will build and run Docker containers for:
   1. Backend - on http://localhost:8000
   2. Frontend - on http://localhost:3000
   3. MongoDB
   4. Mongo Express - on http://localhost:8081 (login: `example_username`, password: `example_password`)
4. Go to http://localhost:3000 and try out react UI or go to http://localhost:8000/docs and try the backend API using Swagger UI
by clicking `Try it out` button in any of two `POST` endpoints
5. To stop all containers press `Ctrl+C` in the Terminal

<hr>

Thanks for your visit, feel free to contact me on [LinkedIn](https://www.linkedin.com/in/daniel-pyrzanowski-77503b251)