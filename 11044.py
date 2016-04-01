import math
while True:
    try:
        cases = int(input())
        for i in range(cases):
            grid = list(map(int, input().split()))
            m, n = grid[0], grid[1]
            s = math.ceil((m-2)/3)*math.ceil((n-2)/3)
            print(s)
    except(EOFError):
        break
