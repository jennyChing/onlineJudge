while True:
    try:
        cho = list(map(int,input().split()))
        M = cho[0]
        N = cho[1]
        print(M*N-1)
    except(EOFError):
        break
