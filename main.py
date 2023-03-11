from board import Board
from game import Game

def main():
    
    board = Board()

    game = Game()

    game.coin_tos()

    board.display()
    while True:
        if board.is_continue(game.player):
            
            X, Y = board.input_rock(game.player)

            reversible_rocks_list = board.reversible_rock_list_around_where_you_specified(X, Y, game.player)

            if board.there_are_place_to_put(X, Y, game.player):
                
                board.reverse_rock_where_you_put(X, Y, game.player)

                board.reverse_rocks_around_you_put(reversible_rocks_list)

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
