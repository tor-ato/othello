import random

from board import Board

class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = Human()
        self.playable_player = 1
        self.player_one_black_or_white = 0
        self.player_two_black_or_white = 0


    def coin_tos(self):
        self.player_one_black_or_white = random.randrange(-1, 2, 2)
        self.player_two_black_or_white = -self.player_one_black_or_white
         

    def change_player(self):
        if self.playable_player == 1:
            self.playable_player = 2
        else:
            self.playable_player = 1

    
    def chose_player(self):
       
       self.chose_vs = True

       while self.chose_vs == True:
            print("コンピュータと対戦したい場合はcmp,人間と対戦したい場合はhumを選択してください。")
            self.computer_or_human = input()

            if self.computer_or_human == "cmp":
                self.vs_player = VsPlayer()
                self.vs_player.change_to_computher()
                
                break

            elif self.computer_or_human == "hum":
                self.vs_player = VsPlayer()
                self.vs_player.change_to_human()

                break

            else:
                print("正しい対戦相手を選択してください。")
                continue      

       return self.vs_player
    

class VsPlayer:
    def __init__(self):
        self.player_instance = Human()

    def chose_place_to_put(self, player, board: Board):
        return self.player_instance.chose_place_to_put(player, board)

    def change_to_computher(self):
        self.player_instance = Computer()

    def change_to_human(self):
        self.player_instance = Human()


class Computer:
    def __init__(self) -> None:
        black_or_white = 0

    def chose_place_to_put(self, player, board: Board):
        k = random.randint(0, board.count_put_able_spots_on_board(player)-1)
        chosen_spot = board.putable_spots_on_board(player)
        print(f'chosen_spot[k][0], chosen_spot[k][1] : {chosen_spot[k][0]} , {chosen_spot[k][1]}')
        re_list = [chosen_spot[k][0], chosen_spot[k][1], player]
        print(f're_list : {re_list}')
        return re_list

    # ↓構造
    # [
    #     [
    #         [3, 3]
    #     ], 
    #     [
    #         [3, 3]
    #     ], 
    #     [
    #         [4, 4]
    #     ], 
    #     [
    #         [4, 4]
    #     ]
    # ]

class Human():
    def __init__(self) -> None:
        black_or_white = 0

    def chose_place_to_put(self, player , board: Board):
        return  board.input_rock(player)
    

    