#!/usr/bin/env python3

# import .
# from . import .
from time import sleep
from random import randint

# Own script imports
from helpers import gameboard_management


def calc_probability(game_board):
    fields = gameboard_management.format_game_board(game_board)
    probability = (fields["free"]) / fields["sum"]
    if probability > 0.5:
        think_about_probability = randint(0, 50)

        if think_about_probability <= 30:
            return True
        else:
            return False
    else:
        riski = randint(0, 10)
        if riski >= 9:
            return True
        return False


def bot_play(game_board, current_plays):
    if current_plays > 0:
        sleep(0.9)
        if calc_probability(game_board):
            return True
        else:
            return False
    else:
        return True


if __name__ == '__main__':
    pass
