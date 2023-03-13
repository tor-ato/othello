from board import Board
from game import Game

def main():
    
    board = Board()
    game = Game()
    game.coin_tos()

    board.display()
    
    while True:
        if board.is_continue(game.player):
            
            X, Y, putable = board.input_rock(game.player)

            if putable:
                board.reverse_rocks(X, Y, game.player)
                game.change_player()

            else:
                print("そこには置けません。適切な座標を指定してください。")
            
            board.display()

            if board.board_is_full():
                board.winner_judge()

        else:
            print("置ける場所がありません")
            if board.vs_player_has_no_place_to_put(game.player):
                break
    
    board.print_winner()

if __name__ == '__main__':
    main()
