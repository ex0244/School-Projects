#!/usr/bin/env python3

# import .
# from . import .
# Own script imports

def create_game_board():
    game_board = {}
    for i in range(1, 7):
        game_board[str(i)] = False

    return game_board


def format_game_board(game_board):
    fields = {"free": 0, "occupied": 0, "sum": 6}
    for place in game_board:
        if game_board[place]:
            fields["occupied"] += 1
        else:
            fields["free"] += 1
    return fields


def game_board_check(game_board: dict, number: int, player_sticks: int):
    if not game_board[str(number)] or number == 6:
        if number == 6:
            player_sticks -= 1
        else:
            game_board[str(number)] = True
            player_sticks -= 1
        return player_sticks, game_board, True
    else:
        return player_sticks, game_board, False


if __name__ == '__main__':
    pass
