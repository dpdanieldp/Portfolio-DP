# DRF Postgres React Notes

`DRFPostgresReactNotes` is a full stack notes application built with Django Rest Framework, PostgreSQL on backend and ReactJS on frontend.

`JWT authentication` is implemented in the service.

The API endpoints  are documented with Swagger documentation.

On startup Django superuser is created with credentials passed in env variables defined in `.env.example`
<hr>

## How to try it out

The project is prepared to be run locally in docker using docker-compose.

1. Install, setup and run [Docker Desktop](https://www.docker.com/)
2. Open Terminal and `cd` to `DRFPostgresReactNotes`
3. run `make up` -this command will build and run Docker containers for:
   1. Backend - on  http://0.0.0.0:8000
   2. Frontend - on http://localhost:3000
   3. PostgreSQL
4. Go to http://localhost:3000 and try out React UI.
Swagger UI API documentation can be found on http://0.0.0.0:8000/api/swagger/
5. To stop all containers press `Ctrl+C` in the Terminal
6. To remove created volumes along with the containers run `make clean`

<hr>

Thanks for your visit, feel free to contact me on [LinkedIn](https://www.linkedin.com/in/daniel-pyrzanowski-77503b251)