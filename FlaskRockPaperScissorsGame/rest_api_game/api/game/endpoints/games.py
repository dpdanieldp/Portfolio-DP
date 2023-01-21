import logging

import flask
from api.game.business import add_gamer_credits, create_gamer_get_id, play_game
from api.game.parsers import game_arguments, pagination_arguments
from api.restx import api
from database.models import Game, Gamer
from flask import request, session
from flask_restx import Resource, fields

log = logging.getLogger(__name__)

ns = api.namespace("game/", description="Operations related to rock-paper-scissors game")

pagination = ns.model(
    "PageOfResults",
    {
        "page": fields.Integer(description="Number of this page of results"),
        "pages": fields.Integer(description="Total number of pages of results"),
        "per_page": fields.Integer(description="Number of items per page of results"),
        "total": fields.Integer(description="Total number of results"),
    },
)

game = ns.model(
    "Game",
    {
        "gamer_id": fields.Integer(required=True, description="Gamer"),
        "gamer_choice": fields.String(required=True, description="Gamer choice"),
        "computer_choice": fields.String(required=True, description="computer choice"),
        "result": fields.Integer(required=True, description="Game result"),
    },
)


page_of_games = ns.inherit("PageOfGames", pagination, {"items": fields.List(fields.Nested(game))})


def _get_gamer_id(game_session: flask.session) -> int:
    gamer_id = game_session.get("gamer_id")
    if not gamer_id:
        gamer_id = create_gamer_get_id()
    game_session["gamer_id"] = gamer_id
    return gamer_id


def _get_gamer_credits(gamer_id: int) -> int:
    gamer = Gamer.query.filter(Gamer.id == gamer_id).one()
    return gamer.credits_count


@ns.route("/")
class GamesCollection(Resource):
    @ns.expect(game_arguments)
    def post(self):
        """
        Plays game, returns result
        """
        gamer_choice = (game_arguments.parse_args(request)).get("choice")
        gamer_id = _get_gamer_id(session)
        gamer_credits = _get_gamer_credits(gamer_id)
        if gamer_credits < 3:
            return {
                "info": f"You have  {gamer_credits} credits. To play you need at least 3 credits."
                f" Add credits first!",
                "success": False,
            }
        return play_game(gamer_id, gamer_choice)

    def put(self):
        """
        Adds credits
        """
        gamer_id = _get_gamer_id(session)
        gamer_credits = _get_gamer_credits(gamer_id)
        response_msg = f"You have {gamer_credits} credits. You can only add credits if you have 0 credits."
        if gamer_credits >= 3:
            return {"info": response_msg, "success": False}
        if 3 > gamer_credits > 0:
            return {
                "info": response_msg + " Unfortunately you can't continue to play",
                "success": False,
            }
        add_gamer_credits(gamer_id)
        return {
            "info": "Credits successfully added! You have 10 credits!",
            "success": True,
        }


@ns.route("archive/<int:year>/")
@ns.route("archive/<int:year>/<int:month>/")
@ns.route("archive/<int:year>/<int:month>/<int:day>/")
class GamesArchiveCollection(Resource):
    @ns.expect(pagination_arguments, validate=True)
    @ns.marshal_with(page_of_games)
    def get(self, year, month=None, day=None):
        """
        Returns list of games from a specified time period.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get("page", 1)
        per_page = args.get("per_page", 10)

        start_month = month if month else 1
        end_month = month if month else 12
        start_day = day if day else 1
        end_day = day + 1 if day else 31
        start_date = "{0:04d}-{1:02d}-{2:02d}".format(year, start_month, start_day)
        end_date = "{0:04d}-{1:02d}-{2:02d}".format(year, end_month, end_day)

        games_query = Game.query.filter(Game.game_datetime >= start_date).filter(Game.game_datetime <= end_date)

        games_page = games_query.paginate(page, per_page, error_out=False)

        return games_page
