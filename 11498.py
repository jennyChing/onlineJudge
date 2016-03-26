'''
Division of Nlogonia
'''
while True:
    try:
        k = int(input())
        if k == 0:
            break
        div = list(map(int, input().split()))
        n, m = div[0], div[1]
        for i in range(k):
            cord = list(map(int, input().split()))
            a, b = cord[0], cord[1]
            if a == n or b == m:
                print("divisa")
            elif a > n and b > m:
                print("NE")
            elif a > n and b < m:
                print("SE")
            elif a < n and b > m:
                print("NO")
            else:
                print("SO")
    except(EOFError):
        break


