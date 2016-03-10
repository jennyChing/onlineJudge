def flip(ns,flips):
    for i in range(0,n-1):
        if ns[i] > ns[i+1]:
            ns[i], ns[i+1] = ns[i+1],ns[i]
            print(i,flips)
            flips = flips + 1
            return flip(ns,flips)
        else:
            return flips
while True:
    try:
        n = int(input())
        ns = list(map(int, input().split()))
        flips = 0
        print("Minimum exchange operations :",flip(ns,flips))
    except(EOFError):
        break
