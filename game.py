import random

class Game:
    def __init__(self):
        self.player = 0

    def coin_tos(self):
        if random.randint(0, 1) == 1:
            self.player = 1
        else:
            self.player = -1
        return self.player

    def change_player(self):
        self.player = -self.player
        return self.player

    