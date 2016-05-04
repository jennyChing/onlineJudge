'''
String

10745 - Dominant Strings

Given two strings s1 and s2, we say that s1 dominates s2 if the (multi)set of characters in s1 is a proper superset of the (multi)set of characters in s2. For instance, “acmicpc” dominates “camp”, but it does not dominate “chimp” or “macpac”. For a set S of strings, we call the strings in S which are not dominated by any string in S the dominant strings of S (even if they do not dominate any strings in S). Now, your task is simply to find all the dominant strings of a set of strings.
'''
def read():
    words = []
    ref = []
    wd_cnt = 0
    while True:
        try:
            w = input()
            ref.append(w)
            words.append({})
            for i in range(len(w)):
                if w[i] not in words[wd_cnt]:
                    words[wd_cnt][w[i]] = 1
                else:
                    words[wd_cnt][w[i]] += 1
            wd_cnt += 1
        except(EOFError):
            return words, ref

if __name__ == '__main__':
    words, ref = read()
    dominate = []
    record = [True] * len(ref)
    for i in range(len(words)):
        for j in range(len(words)):
            for k, v in words[i].items():
                print(i, j, k, v, words[j])
                if i != j and k not in words[j]:
                    #print(words[j], k, i, j)
                    record[i] = False

            #dominate.append(ref[i])
    print(record)
    #for c in dominate:
        #print(c)
