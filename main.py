import random


def display(board):
    # print(board, sep='\n')
    for i in board:
        print(i)


def input_rock(player):
    input_rock = list(map(int,input(f"あなたは{player}です、石を置きたい場所を指定して下さい").split()))
    return input_rock

def count_reversible_rock(board,X,Y,player):
    #入力の周りを判定
    reverse_p = []
    for i in range(-1,2):
        # print(f"before X if : X;{X} i;{i}")
        if (X == 0 and i == -1) or (X == 7 and i == 1):
            continue
        # print(f"after X if : X;{X} i;{i}")
        for j in range(-1,2):
            # print(f"before Y if : X;{X} i;{i} Y;{Y} j;{j}")
            if not(Y == 0 and j == -1) and not(Y == 7 and j == 1):
                # print(f"after Y if : X;{X} i;{i} Y;{Y} j;{j}")
                #判定した内容が相手か判定
                # print(f"X : {X} i : {i} Y : {Y}  : {j}")
                # print(f"-----------------------")

                if board[X + i][Y + j] == -player:
                    # print("test2")
                    #相手だったらその先に自分の色の石があるか判定
                    tmp = []
                    #方向の先へ
                    for g in range(1,8):
                        #0 < 8 は壁の指定i*gでj*g斜めに行く、分からなかったら例示して
                        if 0 < X + (i * g) < 7 and 0 < Y + (j * g) < 7:
                            #斜めに行ってる途中で自分と同じ石があったら、
                            if board[X + (i * g)][Y + (j * g)] == player:
                                #returnする配列に入れる
                                reverse_p += tmp
                                break
                            #もしそうでなかったらtmpの配列にappend
                            else:
                                tmp.append([X + (i * g) , Y + (j * g) ])

    return reverse_p

def count_put_able_spots(board, player):
    count_reversible_rock_list = []
    for l in range(0,8):
        for m in range(0,8):
            if len(count_reversible_rock(board,l,m,player)) > 0:
                count_reversible_rock_list.append(count_reversible_rock(board,l,m,player))
    return len(count_reversible_rock_list)


def init_board():
    board = []
    for _ in range(8):
        board.append([0]*8)

    board[3][3] = 1 #白
    board[4][4] = 1 #白
    # board[3][4] = -1 #黒
    # board[4][3] = -1 #黒
    
    display(board)
    return board


def coin_tos():
    if (random.randint(0,1) == 1):
        player = 1
    else:
        player = -1
    return player

def change_player(player):
     player = -player
     return player

def revers_rocks(reversible_rocks,board):
    for i in reversible_rocks:
        board[i[0]][i[1]] *= -1
    return board

def count_0s_on_board(board):
    count0 = 0
    for i in board:
        for j in i:
            if (j == 0):
                count0 += 1
    return count0

def winner_judge(board):
    one_count = 0
    minus_one_count = 0
    for i in board:
        for j in i:
            if (j == 1):
                one_count += 1
            elif (j == -1):
                minus_one_count += 1
    
    print(f"one_count:{one_count}")
    print(f"minus_one_count:{minus_one_count}")

    if one_count > minus_one_count:
        return 1
    elif minus_one_count > one_count:
        return -1
    elif one_count == minus_one_count:
        return 0





    
def main():
    
    board = init_board()

    # player = coin_tos()
    player = -1



    while True:
        #置ける場所が1個以上なら
        print(count_put_able_spots(board, player))
        if(count_put_able_spots(board, player) > 0):

            X, Y = input_rock(player)
            # display(board)     
            #裏返せる石の数
            reversible_rocks = count_reversible_rock(board, X, Y, player)

            #裏返せる数がゼロより多かったら、XとYが置かれていなかった処理を続ける
            print(f"len(reversible_rocks) : {len(reversible_rocks)}")
            if len(reversible_rocks) > 0:
                #置いた場所を反転
                board[X][Y] = player

                #盤面を反転
                board = revers_rocks(reversible_rocks,board)
                
                #プレイヤー交代
                player = change_player(player)
            elif len(reversible_rocks) == 0:
                print("そこには置けません。適切な座標を指定してください。")
            
            # 盤面表示
            display(board)

            amount_of_0s_on_board = count_0s_on_board(board)
            
            print(f"amount_of_0s_on_board : {amount_of_0s_on_board}")

            if (amount_of_0s_on_board == 0):
                winner_judge()
        else:
            print("置ける場所がありません")
            if(count_put_able_spots(board, -player) == 0):
                break

    
    winner = winner_judge(board)
    
    print(f"ゲーム終了勝者{winner}")


        


if __name__ == '__main__':
    main()
