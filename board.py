
class Board:
    def __init__(self):     
        self.values = [[0] * 8 for _ in range(8)]
        self.values[3][3:5] = 1, -1
        self.values[4][3:5] = -1, 1
        self.winner = 0

    @property
    def display(self):
        for row in self.values:
            print(row)    

    @property
    def _count_zeros(self) -> int:
        return sum(row.count(0) for row in self.values)

    @property
    def winner_judge(self):
        count = self._count_stones
        if count[1] > count[-1]:
            self.winner = 1 
        elif count[-1] > count[1]:
            self.winner = -1
        else:
            self.winner = 0

    @property
    def _count_stones(self) -> dict:
        count = {1: 0, -1: 0, 0: 0}
        for i in self.values:
            for j in i:
                count[j] += 1
        return count


    def _reversible_rock_list_around_where_you_specified(self, x, y, black_or_white):
        reversible_rocks = []
        for i in range(max(0, x-1), min(8, x+2)):
            for j in range(max(0, y-1), min(8, y+2)):
                if self.values[i][j] == black_or_white:
                    continue
                if self.values[i][j] == -black_or_white:
                    tmp_rocks = [[i, j]]
                    for g in range(2, 8):
                        x_ = x + (i-x)*g
                        y_ = y + (j-y)*g
                        if not(0 <= x_ < 8 and 0 <= y_ < 8):
                            break
                        if self.values[x_][y_] == -black_or_white:
                            tmp_rocks.append([x_, y_])
                        elif self.values[x_][y_] == black_or_white:
                            reversible_rocks += tmp_rocks
                            break
                        else:
                            break
        return reversible_rocks
    
    def count_put_able_spots_on_board(self, black_or_white):
        return len(self.putable_spots_on_board(black_or_white))
    
    def putable_spots_on_board(self, black_or_white):
        put_able_spots = []
        for l in range(0, 8):
            for m in range(0, 8):
                if self._count_reversible_rocks_around_sopt(l, m, black_or_white) == 0:
                    continue
                if len(self._reversible_rock_list_around_where_you_specified(l, m, black_or_white)) > 0:
                    put_able_spots.append([l, m])
        return put_able_spots


    def _count_reversible_rocks_around_sopt(self, x, y, black_or_white):
        return len(self._reversible_rock_list_around_where_you_specified(x, y, black_or_white))
    

    def _reverse_rocks_around_you_put(self, reversible_rocks):
        for rock in reversible_rocks:
            row, col = rock
            self.values[row][col] *= -1
    
    def input_rock(self, black_or_white):
        x, y = list(map(int,input(f"あなたは{black_or_white}です、石を置きたい場所を指定して下さい").split()))
        putable = self._count_reversible_rocks_around_sopt(x, y, black_or_white) > 0
        return  x, y, putable
    
    
    def can_continue(self, black_or_white):
       return  self.count_put_able_spots_on_board(black_or_white) > 0
    
    @property
    def is_full(self):
        return self._count_zeros == 0
    
    @property
    def print_winner(self):
        self.winner_judge
        print(f"ゲーム終了勝者{self.winner}")

    
    def vs_player_has_no_place_to_put(self, player_one_black_or_white, player_two_black_or_white):
        return all(self.count_put_able_spots_on_board(player_black_or_white) == 0 for player_black_or_white in [player_one_black_or_white, player_two_black_or_white])
    

    def _reverse_rock_where_you_put(self, x, y, black_or_white):
        self.values[x][y] = black_or_white


    def reverse_rocks(self, x, y, black_or_white):
        reversible_rocks_list = self._reversible_rock_list_around_where_you_specified(x, y, black_or_white)
        self._reverse_rock_where_you_put(x, y, black_or_white)
        self._reverse_rocks_around_you_put(reversible_rocks_list)