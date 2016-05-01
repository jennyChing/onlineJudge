'''
String

902 - Password Search

given the size of the password and the encoded message, determines the password following the strategy given above.  To illustrate your task, consider the following example in which the password size is three (N = 3) and the text message is just ‘baababacb’. The password would then be aba because this is the substring with size 3 that appears most often in the whole text (it appears twice) while the other six different substrings appear only once (baa ; aab ; bab ; bac ; acb).
'''
if __name__ == '__main__':
    while True:
        try:
            w = list(map(str, input().split()))
            #n = int(n)
            pswd = {}
            #for i in range(len(w) - n + 1):
            #    s = ""
            #    for j in range(i, i + n):
            #        s += w[j]
            #    if s not in pswd:
            #        pswd[s] = 1
            #    else:
            #        pswd[s] += 1
            #print(max(pswd, key = pswd.get))
        except(EOFError):
            break
