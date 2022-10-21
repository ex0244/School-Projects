#!/usr/bin/env python3

# import .
# from . import .
# Own script imports
from helpers.printables import seperator
from helpers.utils import logger


def create_players():

    players_db = {}
    while True:
        logger(f"#0{seperator[0]}0#")
        num_of_players = int(input(logger("Please tell me the number of players including bots", level="input")))
        num_of_bots = int(input(logger("How many bots are there?", level="input")))
        if num_of_players <= 0:
            logger(f"{num_of_players} players are not possible.", level="warn")
        elif num_of_bots > num_of_players:
            logger("You can't have more bots than players.", level="warn")
        else:
            break
    logger(f"#0{seperator[0]}0#")
    for player in range(num_of_players - num_of_bots):
        players_db[f"player{player + 1}"] = {"player_sticks": 0, "player_name": "", "bot": False}
    for bot in range(num_of_bots):
        players_db[f"bot{bot + 1}"] = {"player_sticks": 0, "player_name": f"bot#{bot + 1}", "bot": True}

    usernames = []
    for player in players_db:
        logger(seperator[1])
        if not players_db[player]["bot"]:
            logger("Player typ: Analog player", level="info", start="")
            while True:
                username = input(logger(f"{player} please enter a username", level="input"))
                if not username:
                    logger("I need a username please.", level="warn")
                elif username in usernames:
                    logger("This username already exists.", level="warn")
                else:
                    logger(f"Hello {username}", level="info")
                    usernames.append(username)
                    players_db[player]["player_name"] = username
                    break
        else:
            logger("Player typ: Bot", level="info", start="")
            logger(f"Hello {players_db[player]['player_name']}", level="info")

    del usernames

    return players_db, [num_of_players, num_of_bots]


def player_play(player_name, current_plays):
    while True:
        inp = input(logger(f'{player_name} do you want to roll the dice? [y/n]', level="input")).lower()
        if inp == 'n' and current_plays >= 1:
            break
        elif inp == 'n' and current_plays < 1:
            logger(f'{player_name} you must roll the dice at least once.', level="warn")
        else:
            return True
    return False


if __name__ == '__main__':
    pass
