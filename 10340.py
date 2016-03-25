'''
Uva online Judge # 10340 All in all:
Given two strings s and t, you have to decide whether s is a subsequence of t, i.e. if you can remove characters from t such that the concatenation of the remaining characters is s.
'''
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
