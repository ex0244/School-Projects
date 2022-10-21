#!/usr/bin/env python3

# import .
# from . import .
# Own script imports
import super_six_bot

from helpers import printables, gameboard_management, player_management
from helpers.utils import welcome_dialog, dice, chill, print_game_information, logger


class SuperSixGame(object):
    def __init__(self):
        self.game_sticks = 36
        self.winner = False

        welcome_dialog()
        self.players_db, self.players_info = player_management.create_players()
        for player in self.players_db:
            self.players_db[player]["player_sticks"] = self.game_sticks // self.players_info[0]
        self.game_board = gameboard_management.create_game_board()
        chill("to start the game")
        print_game_information(self.players_info, self.game_sticks)

    def game(self, players_db: dict, player: str, player_sticks: int, game_board: dict):

        current_plays = 0

        while players_db[player]["player_sticks"] > 0:
            bot_want_to_dice, player_want_to_dice = False, False
            if players_db[player]["bot"]:
                bot_want_to_dice = super_six_bot.bot_play(game_board, current_plays)
            else:
                player_want_to_dice = player_management.player_play(players_db[player]["player_name"], current_plays)

            if bot_want_to_dice or player_want_to_dice:
                current_plays += 1
                number = dice()
                logger(f'{players_db[player]["player_name"]} rolled a {number}.', level="info")

                player_sticks, game_board, good = gameboard_management.game_board_check(game_board, number,
                                                                                        players_db[player][
                                                                                            "player_sticks"])

                if not good:
                    fields = gameboard_management.format_game_board(game_board)
                    logger(f"{number} was unfortunately already on the board.", level="info")
                    players_db[player]["player_sticks"] = player_sticks + fields["occupied"]
                    return gameboard_management.create_game_board(), players_db, False
                else:
                    players_db[player]["player_sticks"] = player_sticks
            else:
                logger(f'{printables.seperator[1]}')
                logger(f'{players_db[player]["player_name"]} finishes his turn.', level="info")
                players_db[player]["player_sticks"] = player_sticks
                return game_board, players_db, False

        logger(printables.seperator[2])
        logger(f'[WIIINNNNEER!!] {players_db[player]["player_name"]}')
        logger(printables.seperator[2])
        return game_board, players_db, True

    def main(self):
        for player in self.players_db:
            player_name = self.players_db[player]["player_name"]

            logger(f'{player_name}\'s turn.')
            logger(f'{printables.seperator[0]}')
            self.game_board, self.players_db, self.winner = self.game(self.players_db, player, self.players_db[player]["player_sticks"], self.game_board)
            if self.winner:
                break
            logger(f'{player_name} has {self.players_db[player]["player_sticks"]} sticks left.', start="\t")
            logger(f'{printables.seperator[0]}')


if __name__ == '__main__':
    ssg = SuperSixGame()
    while True:
        if ssg.winner:
            break
        ssg.main()
