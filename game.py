
import random

class Game:
    def __init__(self) -> None:
        pass

    def coin_tos(self):
        if (random.randint(0, 1) == 1):
            player = 1
        else:
            player = -1
        return player

    def change_player(self, player):
        player = - player
        return player
