'''
Uva online Judge # 10340 All in all:
Given two strings s and t, you have to decide whether s is a subsequence of t, i.e. if you can remove characters from t such that the concatenation of the remaining characters is s.
'''
while True:
    try:
        words = list(map(str, input().split()))
        s, t = words[0], words[1]
        print(s, t)
        if len(s) <= len(t):
            isIn = True
        # use i and j two pointers to track the progress of checking
        a, b = 0, 0
        while b < len(t)-1 and a < len(s)-1:
            #print(a, b, s[a], t[b], len(s)-1, len(t)-1)
            if b == len(t)-1:
                isIn = False
            if s[a] == t[b]:
                a += 1
                b += 1
            else:
                b += 1
        print("No") if isIn == False else print("Yes")
    except(EOFError):
        break
