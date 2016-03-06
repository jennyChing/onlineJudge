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

        for key, value in c.most_common():

            print(key, value)
    except(EOFError):
        break
