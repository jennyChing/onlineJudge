while True:
    try:
        words = list(map(str, input().split()))
        s = words[0]
        t = words[1]
        if len(s) <= len(t):
            all_in_all = True
        i = 0
        for j in range(0, len(t)):
            if i == len(s):
                break
            if s[i] == t[j]:
                i+=1
        if i == len(s):
            all_in_all = True
        else:
            all_in_all = False
        if all_in_all == True:
            print("Yes")
        else:
            print("No")
    except(EOFError):
        break
