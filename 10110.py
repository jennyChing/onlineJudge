while True:
    try:
        n = int(input())
        if n == 0:
            break
        if n**(.5) %1 ==0:
            print("yes")
        else:
            print("no")
    except(EOFError):
        break
