import random

from flask_restx import reqparse

choices = ("rock", "paper", "scissors")

pagination_arguments = reqparse.RequestParser(bundle_errors=True)
pagination_arguments.add_argument("page", type=int, required=False, default=1, help="Page number", location="args")
pagination_arguments.add_argument(
    "per_page",
    type=int,
    required=False,
    choices=[2, 10, 20, 30, 40, 50],
    default=10,
    help="Results per page",
    location="args",
)

game_arguments = reqparse.RequestParser(bundle_errors=True)
game_arguments.add_argument(
    "choice",
    type=str,
    required=False,
    choices=choices,
    default=random.choice(choices),
    help="Choose your move",
    location="args",
)
