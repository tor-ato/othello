from board import Board
from game import Game

def main():
    
    board = Board()

    player = Game()
    # player = -1
    player = player.coin_tos()

    while True:
        #置ける場所が1個以上なら
        print(board.count_put_able_spots(player))
        if(board.count_put_able_spots(player) > 0):

            X, Y = player.input_rock()
            # display(board)     
            #裏返せる石の数
            reversible_rocks = board.count_reversible_rock(X, Y, player)

            #裏返せる数がゼロより多かったら、XとYが置かれていなかった処理を続ける
            print(f"len(reversible_rocks) : {len(reversible_rocks)}")
            if len(reversible_rocks) > 0:
                #置いた場所を反転
                board[X][Y] = player

                #盤面を反転
                board = board.revers_rocks(reversible_rocks,board)
                
                #プレイヤー交代
                player = player.change_player(player)
            elif len(reversible_rocks) == 0:
                print("そこには置けません。適切な座標を指定してください。")
            
            # 盤面表示
            board.display(board)

            amount_of_0s_on_board = board.count_0s_on_board(board)
            
            print(f"amount_of_0s_on_board : {amount_of_0s_on_board}")

            if (amount_of_0s_on_board == 0):
                board.winner_judge()
        else:
            print("置ける場所がありません")
            if(board.count_put_able_spots(board, -player) == 0):
                break

    
    winner = board.winner_judge(board)
    
    print(f"ゲーム終了勝者{winner}")


if __name__ == '__main__':
    main()
