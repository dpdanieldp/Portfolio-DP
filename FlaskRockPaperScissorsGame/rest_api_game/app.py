import os

import settings
from api.game.endpoints.games import ns as games_namespace
from api.restx import api
from database import db
from flask import Blueprint, Flask

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "planets.db")

DB_NAME = settings.DB_NAME


def configure_app(flask_app):
    # flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config["SECRET_KEY"] = "p8077t0938yugiuehg098ehr"
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config["SWAGGER_UI_DOC_EXPANSION"] = settings.RESTX_SWAGGER_UI_DOC_EXPANSION
    flask_app.config["RESTX_VALIDATE"] = settings.RESTX_VALIDATE
    flask_app.config["RESTX_MASK_SWAGGER"] = settings.RESTX_MASK_SWAGGER
    flask_app.config["ERROR_404_HELP"] = settings.RESTX_ERROR_404_HELP


def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint("api", __name__)
    api.init_app(blueprint)
    api.add_namespace(games_namespace)
    flask_app.register_blueprint(blueprint)
    db.init_app(flask_app)

    from database.models import Game, Gamer

    create_database(flask_app)


def create_database(app):
    if not os.path.exists("rest_api_game/" + DB_NAME):
        db.create_all(app=app)


def main():
    initialize_app(app)
    app.run(debug=settings.FLASK_DEBUG, host="0.0.0.0")


if __name__ == "__main__":
    main()
