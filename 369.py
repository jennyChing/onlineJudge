while True:
    try:
        n = list(map(int, input().split()))
        if n[0] == 0:
            break
        N = n[0]
        M = n[1]
        deno = 1
        mole = 1
        for i in range(1,N-M+1):
            deno = deno * i
        for i in range(M+1, N+1):
            mole = mole * i
        c = mole/deno
        print(N,"things taken", M, "at a time is","{0:.0f}".format(c),"exactly.")
    except(EOFError):
        break
