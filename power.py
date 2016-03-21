def dePower(A,B):
    if B == 0:
        return 1
    elif B == 1:
        return A
    else:
        if B not in memo.keys():
            memo[B] = dePower(A, int(B/2))*dePower(A, B-int(B/2))
        return memo[B]
while True:
    try:
        A = int(input())
        B = int(input())
        memo = {}
        print(dePower(A,B))
        print(A**B)
    except(EOFError):
        break
