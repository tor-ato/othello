import random


def display(board):
    # print(board, sep='\n')
    for i in board:
        print(i)


def input_rock(player):
    input_rock = list(map(int,input(f"{player}、石を置きたい場所を指定して下さい").split()))
    return input_rock

def count_reversible_rock(board,X,Y,player):

    display(board)

    #入力の周りを判定
    reverse_p = []
    for i in range(-1,2):
        for j in range(-1,2):
            #判定した内容が相手か判定
            if board[X + i][Y + j] == -player:
                #相手だったらその先に自分の色の石があるか判定

                tmp = []
                for g in range(1,8):
                    if 0 < X + (i * g) < 8 and 0 < Y + (j * g) < 8:
                        if board[X + (i * g)][Y + (j * g)] == player:
                            reverse_p += tmp
                            break
                        tmp.append([X + i * g , Y + j * g ])
                print("tmp", tmp)
    print("revwrse", reverse_p)              

    return reverse_p


def init_board():
    board = []
    for _ in range(8):
        board.append([0]*8)

    board[3][3] = 1 #白
    board[4][4] = 1 #白
    board[3][4] = -1 #黒
    board[4][3] = -1 #黒
    
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

def end_game(board):
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



def main():
    
    board = init_board()

    # player = coin_tos()
    player = -1

    while True:
        X, Y = input_rock(player)

        #裏返せる石の数
        reversible_rocks = count_reversible_rock(board, X, Y, player)

        #裏返せる数がゼロより多かったら処理を続ける
        if len(reversible_rocks) > 0:
            #置いた場所を反転
            board[X][Y] = player

            #盤面を反転
            board = revers_rocks(reversible_rocks,board)
            
            #プレイヤー交代
            player = change_player(player)
        elif len(reversible_rocks) == 0:
            print("そこには置けません。設置可能な場所を指定してください。")
        
        display(board)

        amount_of_0s_on_board = count_0s_on_board(board)
        
        print(f"amount_of_0s_on_board : {amount_of_0s_on_board}")

        if (amount_of_0s_on_board == 0):
            end_game()

        


if __name__ == '__main__':

    main()
