'''
String -
642 - Word Amalgamation

Input
The input file contains four parts:
    1. a dictionary, which consists of at least one and at most 100 words, one per line;
    2. a line containing ‘XXXXXX’, which signals the end of the dictionary;
    3. one or more scrambled ‘words’ that you must unscramble, each on a line by itself; and
    4. another line containing ‘XXXXXX’, which signals the end of the file.
    All words, including both dictionary words and scrambled words, consist only of lowercase English letters and will be at least one and at most six characters long. (Note that the sentinel ‘XXXXXX’ contains uppercase X’s.) The dictionary is not necessarily in sorted order, but each word in the dictionary is unique.

Output
    For each scrambled word in the input, output an alphabetical list of all dictionary words that can be formed by rearranging the letters in the scrambled word. Each word in this list must appear on a line by itself. If the list is empty (because no dictionary words can be formed), output the line ‘NOT A VALID WORD’ instead. In either case, output a line containing six asterisks to signal the end of the list.
'''
def read():
    dic = []
    words = []
    wd_cnt = 0
    while True:
        w = input()
        if w == 'XXXXXX':
            return dic, words
        words.append({})
        for c in w :
            if c not in words[wd_cnt]:
                words[wd_cnt][c] = 1
            else:
                words[wd_cnt][c] += 1
        dic.append(w)
        wd_cnt += 1

if __name__ == '__main__':
    dic, words = read()
    while True:
        try:
            queries = {}
            same = []
            q = input()
            if q == 'XXXXXX':
                break
            for c in q:
                if c not in queries:
                    queries[c] = 1
                else:
                    queries[c] += 1
            for i in range(len(words)):
               if words[i] == queries:
                   same.append(dic[i])
            same = sorted(same)
            if len(same) == 0:
                print('NOT A VALID WORD')
            else:
                for j in range(len(same)):
                    print(same[j])
            print('******')
        except(EOFError):
            break


