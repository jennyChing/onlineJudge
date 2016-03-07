while True:
    try:
        cases = int(input())
        for i in range(0, cases):
            n = int(input())
            n = int((n*567/9+7492)*235/47 -298)
            print(str(n)[-2])
    except(EOFError):
        break
