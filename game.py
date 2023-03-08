
import random

class Game:
    def __init__(self):
        self.values = 0

    def coin_tos(self):
        if (random.randint(0, 1) == 1):
            self.values = 1
        else:
            self.player = -1
        return self.values

    def change_player(self):
        self.values = -self.values
        return self.values
