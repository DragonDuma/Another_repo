# import math
# import random
# import sys

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

# super() function will create a class that will inherit all the methods and properties from another class:
# The isinstance() function returns True if the specified object is of the specified type, otherwise False.
# If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple.


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(self, letter)

    def get_move(self, game):
        pass
