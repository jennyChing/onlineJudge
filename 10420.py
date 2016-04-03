'''
10420 - List of Conquests:
Input
The input consists of at most 2000 lines. The first line contains a number n, indicating that there will be n more lines. Each following line, with at most 75 characters, contains a country (the first word) and the name of a woman (the rest of the words in the line) Giovanni loved. You may assume that the name of all countries consist of only one word.
Output
The output consists of lines in alphabetical order. Each line starts with the name of a country, followed by the total number of women Giovanni loved in that country, separated by a space.
'''
import collections
cases = int(input())
crty = {}
for n in range(cases):
    w = list(map(str, input().split()))
    c = w[0]
    if c not in crty:
        crty[c] = 1
    else:
        crty[c] += 1
crty = collections.OrderedDict(sorted(crty.items()))
for key, value in crty.items():
    print(key, value)
