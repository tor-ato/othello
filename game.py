import random

from board import Board

class Game:
    def __init__(self, player_one_type: str):
        player_one_color, player_two_color = self.coin_tos()
        if player_one_type not in  ('cmp', 'hum'):
            raise TypeError("Please choose a valid opponent: 'cmp' or 'hum'.")
        if player_one_type == 'cmp':
            self.player_one = VsPlayer(Computer(), player_one_color)
        if player_one_type == 'hum':
            self.player_one = VsPlayer(Human(), player_one_color)
        self.player_two = VsPlayer(Human(), player_two_color)
        self.playable_player = self.player_one


    def coin_tos(self):
        player_one_color = random.randrange(-1, 2, 2)
        player_two_color = -player_one_color
        return player_one_color, player_two_color

    @property
    def change_player(self):
        self.playable_player = self.player_two if self.playable_player == self.player_one else self.player_one    


class VsPlayer:
    def __init__(self, player_instance, player_color):
        self.player_instance = player_instance
        self.__black_or_white = player_color


    @property
    def black_or_white(self):
        return self.__black_or_white


    def choose_spot_to_put(self, black_or_white, board: Board):
        return self.player_instance.choose_spot_to_put(black_or_white, board)


class Computer:
    def __init__(self):
        pass


    def choose_spot_to_put(self, black_or_white, board: Board):
        index = random.randint(0, board.count_put_able_spots_on_board(black_or_white)-1)
        chosen_spot = board.putable_spots_on_board(black_or_white)[index]
        return [chosen_spot[0], chosen_spot[1], black_or_white]


class Human:
    def __init__(self):
        pass


    def choose_spot_to_put(self, black_or_white, board: Board):
        return  board.input_rock(black_or_white)