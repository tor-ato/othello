from game import Game

class Board:
    def __init__(self):
        self.values = []
        for _ in range(8):
            self.values.append([0]*8)
        
        self.values[3][3] = 1
        self.values[4][4] = 1
        self.values[3][4] = -1
        self.values[4][3] = -1

        self.winner = 0



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
            self.winner = 1 
        elif minus_one_count > one_count:
            self.winner = -1
        else:
            self.winner = 0


    def reversible_rock_list_around_where_you_specified(self, X, Y, player):
        #入力の周りを判定
        reverse_p = []

        for i in range(-1,2):

            # 0 and -1 か 7 and 1 ならforループをスキップ
            if (X == 0 and i == -1) or (X == 7 and i == 1):
                continue
            
            for j in range(-1,2):

                # 0 and -1 か 7 and 1 ならforループをスキップ
                if (Y == 0 and j == -1) or (Y == 7 and j == 1):
                    continue
                
                # 石が自分の石の場合はforループをスキップ
                if self.values[X + i][Y + j] ==  player:
                    continue
                
                #self.values[X + i][Y + j]が相手だったら
                tmp = []
                
                #方向の先へ進む
                for g in range(1, 8):

                    #0 < 8 は壁の指定i*gでj*g斜めに行く、分からなかったら例示して
                    if not( 0 < X + (i * g) < 7 and 0 < Y + (j * g) < 7):
                        continue

                    #斜めに行ってる途中で自分違う石があったら、その石の情報をtmpに追加
                    if self.values[X + (i * g)][Y + (j * g)] == -player:
                        tmp.append([X + (i * g) , Y + (j * g) ])
                    
                    elif self.values[X + (i * g)][Y + (j * g)] == player and tmp != []:
                        #returnする配列に入れる
                        reverse_p += tmp
                        break

                    else:
                        break
        return reverse_p
        
    def count_put_able_spots_on_board(self, player):
        reversible_rock_list_on_board = []
        for l in range(0, 8):
            for m in range(0, 8):
                if self.count_reversible_rocks_around_sopt(l, m, player) > 0:
                    reversible_rock_list_on_board.append(self.reversible_rock_list_around_where_you_specified(l, m, player))       
        return len(reversible_rock_list_on_board)
    

    def count_reversible_rocks_around_sopt(self, x, y, player):
        return len(self.reversible_rock_list_around_where_you_specified(x, y, player))
    

    def reverse_rocks_around_you_put(self, reversible_rocks):
        for i in reversible_rocks:
            self.values[i[0]][i[1]] *= -1

    
    
    def input_rock(self, player):
        x, y = list(map(int,input(f"あなたは{player}です、石を置きたい場所を指定して下さい").split()))
        putable = self.count_reversible_rocks_around_sopt(x, y, player) > 0
        return  x, y, putable
    
    
    def is_continue(self, player):
       return  (self.count_put_able_spots_on_board(player) > 0)
    
    
    def board_is_full(self):
        amount_of_zeros_on_board = self.count_zeros()
        return amount_of_zeros_on_board == 0
    
    
    def print_winner(self):
        self.winner_judge()
        print(f"ゲーム終了勝者{self.winner}")

    
    def vs_player_has_no_place_to_put(self, player):
        return self.count_put_able_spots_on_board(-player) == 0
    
    def reverse_rock_where_you_put(self, x, y, player):
        self.values[x][y] = player

    def reverse_rocks(self, X, Y, player):
        reversible_rocks_list = self.reversible_rock_list_around_where_you_specified(X, Y, player)
        self.reverse_rock_where_you_put(X, Y, player)
        self.reverse_rocks_around_you_put(reversible_rocks_list)


    