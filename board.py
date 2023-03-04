
class Board:
    def __init__(self):
        self.values = []
        for _ in range(8):
            self.values.append([0]*8)
        
        self.values[3][3] = 1
        self.values[4][4] = 1
        self.values[3][4] = -1
        self.values[4][3] = -1

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
        
    def display(self):
        for i in self.values:
            print(i)