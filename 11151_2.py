'''

Palindrome

11151 - Longest Palindrome

For each input string, your program should print the length of the longest palindrome you can get by removing zero or more characters from it.
'''
def pal(word):
    lst = {}
    index = (0, 0)
    length = len(word)
    if length <= 1:
        return index
    temp = str()
    for x, y in enumerate(word):
        t = x
        for i in range(x):
            if i != t + 1:
                string = word[i:t + 1]
                if string == string[::-1]:
                    temp = word[i: t + 1]
                    index = (i, t + 1)
                    lst[temp] = index
    tat = lst.keys()
    longest = max(tat, key=len)
    return lst[longest], temp

if __name__ == '__main__':
    cases = int(input())
    print(cases)
    for _ in range(cases):
        word = input()
        print(word)
        len_pal, pali = pal(word)
        print(len_pal[1])

