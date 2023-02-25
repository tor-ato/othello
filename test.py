

def main():
    test_list = []
    for _ in range(3):
        test_list.append([0]*3)

    
    print(*test_list,sep='\n')
    test_list[0][0] = -2
    print(*test_list,sep='\n')

    for i in range(-1,2):
        for j in range(-1,2):
            test_list[X-i][Y-j] == 1 or -1

    print(*test_list,sep='\n')

if __name__ == '__main__':
    main()