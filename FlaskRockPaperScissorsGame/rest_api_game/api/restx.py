import logging
import traceback

import settings
from flask_restx import Api
from sqlalchemy.orm.exc import NoResultFound

log = logging.getLogger(__name__)

api = Api(
    version="1.0",
    title="Rock-paper-scissors game",
    description="""A simple REST API game
    
    Game rules:
1. Each new session is a new player. 
2. Each game costs the player 3 credits.
3. A winning game adds 4 credits to the player.
4. A player can add 10 credits to own account, in case the player has 0 of them.
5. Each game has statistics collected (winning, losing, player ID, time game, number of credits before the game). 
6. The application allows you to view statistics for a given day""",
)


@api.errorhandler
def default_error_handler(e):
    message = "An unhandled exception occurred."
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {"message": message}, 500


@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    """No results found in database"""
    log.warning(traceback.format_exc())
    return {"message": "A database result was required but none was found."}, 404
