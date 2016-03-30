'''
11764 Jumping Mario: Easy
'''
case = 0
while True:
    try:
        cases = int(input())
        for i in range(cases):
            case += 1
            n = int(input())
            walls = list(map(int, input().split()))
            h, l = 0, 0
            for j in range(len(walls)-1):
                if walls[j] < walls[j+1]:
                    h += 1
                elif walls[j] > walls[j+1]:
                    l += 1
            print("Case ", case, ": ", sep="", end="")
            print(h, l)

    except(EOFError):
        break
