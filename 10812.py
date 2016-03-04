while True:
    try:
        cases = int(input())
        for i in range(0, cases):
            scores = list(map(int, input().split()))
            X = sum(scores)/2
            Y = scores[0] - X
            if X%1 == 0 and Y%1 == 0 and X >= 0 and Y >= 0:
                print("{0:.0f}".format(X),"{0:.0f}".format(Y))
            else:
                print("impossible")
    except(EOFError):
        break
