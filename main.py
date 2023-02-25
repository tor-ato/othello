def display(board):
    # print(board, sep='\n')
    for i in board:
        print(i)


def input_rock(player):
    input_rock = list(map(int,input(f"{player}、石を置きたい場所を指定して下さい").split()))
    return input_rock

def reversible_rock(board,X,Y,player):
    sentinel = 0
    go_strait_check = True

    display(board)

    #入力の周りを判定
    reverse_p = []
    for i in range(-1,2):
        for j in range(-1,2):
            print("case" ,i, j)
            #判定した内容が相手か判定
            if board[X + i][Y + j] == -player:
                #相手だったらその先に自分の色の石があるか判定

                tmp = []
                for g in range(1,8):
                    if 0 < X + i * g < 8 and 0 < Y + j * g < 8:
                        if board[X + i * g][Y + j * g] == player:
                            reverse_p += tmp
                            break
                        tmp.append([X + i * g , Y + j * g ])
                print("tmp", tmp)
    print("revwrse", reverse_p)              

    return reverse_p



def main():
    board = []
    for _ in range(8):
        board.append([0]*8)

    board[3][3] = 1 #白
    board[4][4] = 1 #白
    board[3][4] = -1 #黒
    board[4][3] = -1 #黒

    player = 1 # 白1 黒-1
    game = True # 1ゲーム中　0ゲーム終了

    while game == True:

        display(board)
        rock_position = input_rock(player)
        X =rock_position[0]
        Y =rock_position[1]
        # rock_set_board = set_rock(board,X,Y,player)
        # print(rock_set_board)

def test():
    board = []
    for _ in range(8):
        board.append([0]*8)

    board[3][3] = 1 #白
    board[4][4] = 1 #白
    board[3][4] = -1 #黒
    board[4][3] = -1 #黒


    display(board)

    player = 1
    while True:
        rock = input_rock(player)
        X = rock[0]
        Y = rock[1]

        revece_p = reversible_rock(board, X, Y, player)

        if len(revece_p) > 0:
            board[X][Y] = player

            for p in revece_p:
                board[p[0]][p[1]] *= -1

        display(board)

        player = -player


if __name__ == '__main__':
    # main()
    test()
