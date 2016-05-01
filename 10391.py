'''
String

10391 - Compound Words

You are to find all the two-word compound words in a dictionary. A two-word compound word is a word in the dictionary that is the concatenation of exactly two other words in the dictionary.
'''
def read():
    words = []
    dic = set()
    while True:
        try:
            w = input()
            words.append(w)
            dic.add(w)
        except(EOFError):
            return words, dic

if __name__ == '__main__':
    words, dic = read()
    compound = []
    for i in range(len(words)):
        for j in range(1, len(words[i])):
            l = words[i][:j]
            r = words[i][j:]
            if l in dic and r in dic:
                compound.append(words[i])
                break
    for c in compound:
        print(c)




