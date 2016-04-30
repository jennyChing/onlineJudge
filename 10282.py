'''
String
10282 - Babelfish

Input
Input consists of up to 100,000 dictionary entries, followed by a blank line, followed by a message of up to 100,000 words. Each dictionary entry is a line containing an English word, followed by a space and a foreign language word. No foreign word appears more than once in the dictionary. The message is a sequence of words in the foreign language, one word on each line. Each word in the input is a sequence of at most 10 lowercase letters.

Output
Output is the message translated to English, one word per line. Foreign words not in the dictionary should be translated as ‘eh’.
'''
if __name__ == '__main__':
    dic = []
    while True:
        try:
            w = list(map(str, input().split()))
            if len(w) == 1:
                print(w[0], w[0] in dic)
                print(dic[w]) if w[0] in dic else print('eh')
            else:
                dic.append({w[1]: w[0]})
                print(dic)

        except(EOFError):
            break

