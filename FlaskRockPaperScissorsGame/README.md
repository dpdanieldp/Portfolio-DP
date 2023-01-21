# Flask Rock-Paper-Scissors Game

`FlaskRockPaperScissorsGame` is an HTTP API built with Flask with Swagger UI documentation.

Game rules:
1. Each new session is a new player. 
2. Each game costs the player 3 credits.
3. A winning game adds 4 credits to the player.
4. A player can add 10 credits to own account, in case the player has 0 of them.
5. Each game has statistics collected (winning, losing, player ID, time game, number of credits before the game). 
6. The application allows you to view statistics for a given day

<hr>

## How to try it out

The project is prepared to be run locally in docker using docker-compose.

1. Install, setup and run [Docker Desktop](https://www.docker.com/)
2. Open Terminal and `cd` to `FlaskRockPaperScissorsGame`
3. Build Docker image:
```bash
$ docker image build -t flask_game . 
```
4. Run docker container:
```bash
$ docker run -p 5000:5000 -d flask_game
```
5. Go to http://localhost:5000 and play game using Swagger UI

<hr>

Thanks for your visit, feel free to contact me on [LinkedIn](https://www.linkedin.com/in/daniel-pyrzanowski-77503b251)