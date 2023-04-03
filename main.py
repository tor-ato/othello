from board import Board
from game import Game
from game import VsPlayer

def main():
    
    board = Board()
    game = Game()
    game.coin_tos()

    game.player_one:VsPlayer = game.chose_player()


    board.display()

    while True:
        # print(f'board.can_continue(game.player_one_black_or_white) : {game.player_one_black_or_white}')
        # print(f'board.can_continue(game.player_two_black_or_white) : {game.player_two_black_or_white}')


        # print(f'board.can_continue(game.player_one_black_or_white) : {board.can_continue(game.player_one_black_or_white)}')
        # print(f'board.can_continue(game.player_two_black_or_white) : {board.can_continue(game.player_two_black_or_white)}')



        if board.can_continue(game.player_one_black_or_white) == False or board.can_continue(game.player_two_black_or_white) == False:
            break
        


        print(f'game.playable_player : {game.playable_player}')

        if game.playable_player == 1:
            # msg = vs_player.chose_place_to_put(game.player_one_black_or_white, board)
            # print(f'chose_place_to_put : {msg}')
            print(f'game.player_one : {type(game.player_one)}')

            X, Y, putable = game.player_one.chose_place_to_put(game.player_one_black_or_white, board)
            
            print(f'')

            if putable:
                board.reverse_rocks(X, Y, game.player_one_black_or_white)
                game.change_player()

            else:
                print("そこには置けません。適切な座標を指定してください。")

            board.display()

            if board.is_full():
                board.winner_judge()
        
       
        elif game.playable_player == 2:

            print(f'game.player_two : {type(game.player_two)}')
            X, Y, putable = game.player_two.chose_place_to_put(game.player_two_black_or_white, board)

            if putable:
                board.reverse_rocks(X, Y, game.player_two_black_or_white)
                game.change_player()

            else:
                print("そこには置けません。適切な座標を指定してください。")

            board.display()

            if board.is_full():
                board.winner_judge()

        else:
            print("置ける場所がありません")
            print(board.vs_player_has_no_place_to_put(game.player_one_black_or_white, game.player_two_black_or_white))
            if board.vs_player_has_no_place_to_put(game.player_one_black_or_white, game.player_two_black_or_white):
                break
    
    board.print_winner()

if __name__ == '__main__':
    main()
