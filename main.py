from board import Board
from game import Game

def main():
    
    board = Board()

    game = Game()
    # game = -1
    game.coin_tos()

    board.display()
    while True:
        #置ける場所が1個以上なら
        if(board.is_continue(game.player) > 0):
            
            X, Y = board.input_rock(game.player)
            # display(board)     
            #裏返せる石の数
            
            reversible_rocks = board.count_reversible_rock(X, Y, game.player)

            #裏返せる数がゼロより多かったら、XとYが置かれていなかった処理を続ける
            print(f"len(reversible_rocks) : {len(reversible_rocks)}")
            if len(reversible_rocks) > 0:
                #置いた場所を反転
                board.values[X][Y] = game.player

                #盤面を反転
                board.reverse_rocks(reversible_rocks)
                
                #プレイヤー交代
                game.change_player()
            elif len(reversible_rocks) == 0:
                print("そこには置けません。適切な座標を指定してください。")
            
            # 盤面表示
            board.display()

            amount_of_zeros_on_board = board.count_zeros()
            
            print(f"amount_of_0s_on_board : {amount_of_zeros_on_board}")

            if (amount_of_zeros_on_board == 0):
                board.winner_judge()
        else:
            print("置ける場所がありません")
            if(board.count_put_able_spots(-game.player) == 0):
                break
    
    winner = board.winner_judge()
    
    print(f"ゲーム終了勝者{winner}")


if __name__ == '__main__':
    main()
