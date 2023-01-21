import random

from database import db
from database.models import Game, Gamer


def create_gamer_get_id() -> int:
    gamer = Gamer()
    db.session.add(gamer)
    db.session.commit()
    return gamer.id


def play_game(gamer_id: int, gamer_choice: str) -> dict:
    valid_choices = ["rock", "paper", "scissors"]
    valid_choices.remove(gamer_choice)
    computer_choice = random.choice(valid_choices)
    gamer = Gamer.query.filter(Gamer.id == gamer_id).one()

    result = _get_game_result(gamer_choice, computer_choice)

    game = Game(
        gamer_choice=gamer_choice,
        computer_choice=computer_choice,
        result=result,
        gamer_id=gamer_id,
        gamer_credits_before_game=gamer.credits_count,
    )
    if result:
        gamer.credits_count += 1
    else:
        gamer.credits_count -= 3
    db.session.add(game)
    db.session.commit()
    response = {
        "gamer_id": gamer_id,
        "gamer_choice": gamer_choice,
        "computer_choice": computer_choice,
        "game_result": "You win!" if result == 1 else "You lose!",
        "gamer_credits": gamer.credits_count,  # credits after game
    }
    return response


def _get_game_result(gamer_choice, computer_choice) -> int:
    wins = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper",
    }
    if wins[gamer_choice] == computer_choice:
        return 1
    return 0


def add_gamer_credits(gamer_id: int):
    gamer = Gamer.query.filter(Gamer.id == gamer_id).one()
    gamer.credits_count = 10
    db.session.commit()
