while True:
    memo = {}
    try:
        line = int(input())
        for i in range(0,line):
            words = input().upper()
            for c in words:
                if c.isalpha() == True and c in memo:
                    memo[c] = memo[c]+1
                elif c.isalpha() == True and c not in memo:
                    memo[c]=1
        print(memo)
    except(EOFError):
        break
