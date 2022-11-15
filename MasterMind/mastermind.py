#!/usr/bin/env python3

import random

class MasterMind(object):
    def __init__(self):
        self.colors = ["green", "red", "yellow", "black", "blue", "pink", "gray", "brown"]  # Colors used in the codes
        self.code_len = 4  # Number of colors in the code
        self.number_of_guesses = 8  # Number of available guesses
        self.banner = f"""+-----------------------------------------------------------------------+
|   Lets play Mastermind. A game in which the player has to guess a     |
|   code made up of colors. The ouput of each round will give hints to  | 
|   the actual code:                                                    |
|   * -> Right place, right color                                       |
|   + -> Right color, wrong place                                       |
|   _ -> Wrong place, wrong color                                       |
|                                                                       |
|   The colors are: {", ".join(self.colors).ljust(52)}|
|   The code length will be: {str(self.code_len).ljust(43)}|
|   The number of available guesses will be: {str(self.number_of_guesses).ljust(27)}|
+-----------------------------------------------------------------------+
"""

    def gen_code(self, scmt: bool) -> list:
        if not scmt:
            code = []
            for _ in range(self.code_len):
                color = self.colors[random.randint(0, len(self.colors) - 1)]
                while color in code:
                    color = self.colors[random.randint(0, len(self.colors) - 1)]
                code.append(color)
        else:
            code = [self.colors[random.randint(0, len(self.colors) - 1)] for _ in range(self.code_len)]

        return code

    def gen_result(self, inp: list, code: list, pd: bool) -> list:
        result = []

        for index, color in enumerate(inp):
            if color in code:
                if color == code[index]:
                    result.append("*")
                else:
                    result.append("+")
            else:
                result.append("_")
        
        if not pd:
            result.sort()

        return result

    def check_result(self, output: str) -> bool:
        if output == "*" * self.code_len:
            return True

    def config(self) -> dict:
        config = {"scmt": False, "pd": False}
        scmt = input("Do you allow the code to have the same color multiple times (harder)? [y/N]> ").lower()
        if scmt == "y":
            config["scmt"] = True

        pd = input("Do you want your hints position dependend (easier)? [y/N]> ").lower()
        if pd == 'y':
            config["pd"] = True

        return config

    def main(self):
        print(self.banner)
        config = self.config()
        code = self.gen_code(config["scmt"])
        for i in range(self.number_of_guesses):
            while True:
                inp = input(f"{i + 1}. # Input (Format: <color1>, <color2>, ...) - {self.code_len} Colors> ").split(", ")
                if len(inp) != self.code_len: 
                    print(f"The input must have a length of {self.code_len} characters!")
                    continue
                else:
                    break
            # l = self.gen_result(inp, code, config["pd"])
            result = "".join(self.gen_result(inp, code, config["pd"]))
                
            if config["pd"]:
                print("Result (position dependend): ", result)
            else:
                print("Result (NOT position dependend): ", result)
            if self.check_result(result):
                print("You win..")
                exit()
        print(f"You lose..\nSolution: {code}")

if __name__ == '__main__':
    mm = MasterMind()
    mm.main()


