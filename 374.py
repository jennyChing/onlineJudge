def cal_mod (B,P,M):
    if P == 0:
        return 1
    if P % 2:
        return ((B%M)*(cal_mod(B,P-1,M)))%M
    else:
        c = cal_mod(B,P/2,M)
        return ((c%M)*(c%M))%M
B = int(input())
P = int(input())
M = int(input())
print(cal_mod(B,P,M))
while True:
    try:
        for i in range(0,4):
            n = input()
            B = int(input())
            P = int(input())
            M = int(input())
            print(cal_mod(B,P,M))
    except(EOFError):
        break
