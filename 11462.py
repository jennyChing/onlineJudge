while True:
    try:
        n = int(input())
        if n == 0:
            break
        ages = list(map(int, input().split()))
        ages = sorted(ages)
        for i in range(len(ages)-1):
            print(ages[i], "",end="")
        print(ages[-1])
    except(EOFError):
        break
