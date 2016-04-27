'''
String - Data Structure: Binary Search Tree
156 - Ananagrams

 no matter how you rearrange their letters, you cannot form another word. Such words are called ananagrams, an example is QUIZ.

 Input

 Input will consist of a series of lines. No line will be more than 80 characters long, but may contain any number of words. Words consist of up to 20 upper and/or lower case letters, and will not be broken across lines. Spaces may appear freely around words, and at least one space separates multiple words on the same line. Note that words that contain the same letters but of differing case are considered to be anagrams of each other, thus tIeD and EdiT are anagrams. The file will
 be terminated by a line consisting of a single #.

 Output

 Output will consist of a series of lines. Each line will consist of a single word that is a relative ananagram in the input dictionary. Words must be output in lexicographic (case-sensitive) order. There will always be at least one relative ananagram.

Solution:
    Loop through the dictionary and add the pairs that are anagrams of each other in to a new group. Result is to print all except of the new group.
'''

def read():
    words = []
    wd_cnt = 0
    while True:
        line = list(map(str, input().split()))
        if line == ['#']:
            return words
        for i in range(len(line)):
            for c in line[i]:
                words.append({})
                if c not in words[wd_cnt]:
                    words[wd_cnt][c] = 1
                else:
                    words[wd_cnt][c] += 1
            wd_cnt += 1

if __name__ == '__main__':
    print(read())





