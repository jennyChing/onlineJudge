'''
String

10391 - Compound Words

Given two strings s1 and s2, we say that s1 dominates s2 if the (multi)set of characters in s1 is a proper superset of the (multi)set of characters in s2. For instance, “acmicpc” dominates “camp”, but it does not dominate “chimp” or “macpac”. For a set S of strings, we call the strings in S which are not dominated by any string in S the dominant strings of S (even if they do not dominate any strings in S). Now, your task is simply to find all the dominant strings of a set of strings.
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
    print(dic)
    compound = []
    for i in range(len(words)):
        for j in range(1, len(words[i])):
            l = words[i][:j]
            r = words[i][j:]
            print(l, r)
            if l in dic or r in dic:
                compound.append(words[i])
                break
    for c in compound:
        print(c)
