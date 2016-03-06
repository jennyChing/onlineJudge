from collections import Counter, OrderedDict
while True:
    try:
        line = int(input())
        c = Counter()
        for i in range(0,line):
            words = input()
            for al in words:
                if al.isalpha() == True:
                    c[al.upper()]+=1
        sorted_key = sorted(c.items(),key=lambda sl: (sl[0]))
        sorted_value = sorted(sorted_key, key = lambda sl: (sl[1]),reverse=True)
        for key, value in sorted_value:
            print(key, value)
    except(EOFError):
        break
