#!/usr/bin/env python3

# import .
# from . import .
from random import randint

# Own script imports
import helpers.printables


def dice():
    return randint(1, 6)


def logger(msg, level="normal", start="  ", *args, **kwargs):
    if level == "normal":
        print(msg)  # normal
    elif level == "info":
        print("{}[?] Info: {}".format(start, msg), *args, *kwargs)  # [?] Info: info
    elif level == "input":
        return "[~] Input: {} > ".format(msg)  # [?] Info: info
    elif level == "error":
        print("{}[!] Error: {}".format(start, msg), *args, *kwargs)  # [!] Error: error
    elif level == "success":
        print("{}[+] Success: {}".format(start, msg), *args, *kwargs)  # [+] Success: success
    elif level == "warn":
        print("{}[*] Warn: {}".format(start, msg), *args, *kwargs)  # [*] Warn: warning


def chill(what: str):
    input(f"\nPlease press [SPACE] {what}")


def welcome_dialog():
    print(helpers.printables.banner)
    chill("to start the game setup.")


def print_game_information(num_of_players, num_of_bots):
    print(helpers.printables.players_menu(num_of_players, num_of_bots))


if __name__ == '__main__':
    pass
