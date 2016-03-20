def count_inversion(ns):
    count = 0
    if ns == 1:
        count = 0
    for i in range(0, len(ns)):
        for j in range(i+1, len(ns)):
            if ns[i] > ns[j]:
                count = count + 1
    return(count)
while True:
    try:
        n = input()
        if len(n) == 0:
            break
        else:
            ns = list(map(int, input().split()))
            print("Minimum exchange operations :",count_inversion(ns))
    except(EOFError):
        break
