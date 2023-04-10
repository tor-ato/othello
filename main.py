from board import Board
from game import Game
from game import VsPlayer

def main():
    board = Board()

    while True:
        print("コンピュータと対戦したい場合はcmp,人間と対戦したい場合はhumを選択してください。")
        player_one_type = input()
        if player_one_type not in ('cmp', 'hum'):
            print("そこには置けません。適切な座標を指定してください。")
            continue
        game = Game(player_one_type)
        break

    board.display

    while True:
        if not board.can_continue(game.player_one.black_or_white) or not board.can_continue(game.player_two.black_or_white):
            break

        X, Y, putable = game.playable_player.choose_spot_to_put(game.playable_player.black_or_white, board)
        if putable:
            board.reverse_rocks(X, Y, game.playable_player.black_or_white)
            game.change_player
        else:
            print("そこには置けません。適切な座標を指定してください。")

        board.display

        if board.is_full:
            board.winner_judge()
        
        if board.vs_player_has_no_place_to_put(game.player_one.black_or_white, game.player_two.black_or_white):
            print("置ける場所がありません")
            break

    board.print_winner

if __name__ == '__main__':
    main()