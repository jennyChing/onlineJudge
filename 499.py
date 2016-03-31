import operator

while True:
    try:
        content = input()
        memo = {}
        for c in content:
            if c.isalpha():
                if c in memo:
                    memo[c] += 1
                else:
                    memo[c] = 1
        v = list(memo.values())
        k = list(memo.keys())
        c = []
        for i in range(len(v)):
            if v[i] == max(v):
                c.append(k[i])
        c = sorted(c)
        print(''.join(c), max(v))
    except(EOFError):
        break
