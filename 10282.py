'''
String
10282 - Babelfish

Input
Input consists of up to 100,000 dictionary entries, followed by a blank line, followed by a message of up to 100,000 words. Each dictionary entry is a line containing an English word, followed by a space and a foreign language word. No foreign word appears more than once in the dictionary. The message is a sequence of words in the foreign language, one word on each line. Each word in the input is a sequence of at most 10 lowercase letters.

Output
Output is the message translated to English, one word per line. Foreign words not in the dictionary should be translated as ‘eh’.
'''

def read_words():
    dic = {}
    while True:
        w = list(map(str, input().split()))
        if len(w) == 0:
            return dic
        else:
            dic[w[1]] = w[0]


if __name__ == '__main__':
    dic = read_words()
    while True:
        try:
            q = input()
            print(dic[q]) if q in dic else print('eh')
        except(EOFError):
            break

