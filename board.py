from game import Game

class Board:
    #テストしなくていい
    def __init__(self):
        self.values = []
        for _ in range(8):
            self.values.append([0]*8)
        
        self.values[3][3] = 1
        self.values[4][4] = 1
        self.values[3][4] = -1
        self.values[4][3] = -1


    def display(self):
        for i in self.values:
            print(i)

    def count_zeros(self) -> int:
        count_zero = 0
        for i in self.values:
            for j in i:
                if (j == 0):
                    count_zero += 1

        return count_zero

    
    def winner_judge(self):
        one_count = 0
        minus_one_count = 0
        for i in self.values:
            for j in i:
                if(j == 1):
                    one_count += 1
                elif (j == -1):
                    minus_one_count += 1
        
        if one_count > minus_one_count:
            return 1 
        elif minus_one_count > one_count:
            return -1
        else:
            return 0


    def count_reversible_rock(self, X, Y, player):
        #入力の周りを判定
        reverse_p = []
        for i in range(-1,2):
            if (X == 0 and i == -1) or (X == 7 and i == 1):
                continue
            for j in range(-1,2):
                if not(Y == 0 and j == -1) and not(Y == 7 and j == 1):
                    #判定した内容が相手か判定
                    if self.values[X + i][Y + j] == - player:
                        #相手だったらその先に自分の色の石があるか判定
                        tmp = []
                        #方向の先へ
                        for g in range(1,8):
                            #0 < 8 は壁の指定i*gでj*g斜めに行く、分からなかったら例示して
                            if 0 < X + (i * g) < 7 and 0 < Y + (j * g) < 7:
                                #斜めに行ってる途中で自分と同じ石があったら、
                                if self.values[X + (i * g)][Y + (j * g)] == player:
                                    #returnする配列に入れる
                                    reverse_p += tmp
                                    break
                                #もしそうでなかったらtmpの配列にappend
                                else:
                                    tmp.append([X + (i * g) , Y + (j * g) ])
        print(f"reverse_p : {reverse_p}")
        return reverse_p    

    def count_put_able_spots(self, player):
        count_reversible_rock_list = []
        for l in range(0,8):
            for m in range(0,8):
                if len(self.count_reversible_rock(l, m, player)) > 0:
                    count_reversible_rock_list.append(self.count_reversible_rock(l, m, player))
        return len(count_reversible_rock_list)

    def reverse_rocks(self, reversible_rocks):
        for i in reversible_rocks:
            self.values[i[0]][i[1]] *= -1
    
    def input_rock(self, player):
        return list(map(int,input(f"あなたは{player}です、石を置きたい場所を指定して下さい").split()))