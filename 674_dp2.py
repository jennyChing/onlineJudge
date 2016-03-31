def cal(i, change, table):
    coins = [1, 5, 10, 25, 50]
    try:
        if change - coins[i] >= 0:
            table[i].append(table[i-1][change] + table[i][change-coins[i]])
        else:
            table[i].append(table[i-1][change])
    except(IndexError):
        pass
t_size = 0
table = [[1 for x in range(t_size+1)] for x in range(5)]
if __name__ == '__main__':
    while True:
        try:
            change = int(input())
# only calculate and append results that are not in the current table
            if change > t_size:
                for i in range(1,5):
                    for j in range(t_size+1,change+1):
                        table[0].append(1)
                        cal(i, j, table)
                t_size = change
                print(table[-1][-1])
            else:
                print(table[-1][change])
        except(EOFError):
            break
