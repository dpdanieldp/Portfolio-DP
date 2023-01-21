from datetime import datetime

from . import db


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gamer_credits_before_game = db.Column(db.Integer)
    gamer_choice = db.Column(db.String(10))
    computer_choice = db.Column(db.String(10))
    result = db.Column(db.Integer)  # 0- gamer lose 1- gamer won
    game_datetime = db.Column(db.DateTime)

    gamer_id = db.Column(db.Integer, db.ForeignKey("gamer.id"))

    def __init__(
        self,
        gamer_choice: str,
        computer_choice: str,
        result: int,
        gamer_id: int,
        gamer_credits_before_game: int,
    ):
        self.gamer_choice = gamer_choice
        self.game_datetime = datetime.utcnow()
        self.computer_choice = computer_choice
        self.gamer_credits_before_game = gamer_credits_before_game
        self.result = result
        self.gamer_id = gamer_id


class Gamer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    credits_count = db.Column(db.Integer)
    game = db.relationship("Game")

    def __init__(self):
        self.credits_count = 10
