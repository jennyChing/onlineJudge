'''

Palindrome

10453 - Make Palindrome

You can easily verify that for a string of length n, no more than (n−1) characters are required to make it a palindrome. Consider ‘abcd’ and its palindrome ‘abcdcba’ or ‘abc’ and its palindrome ‘abcba’.  But life is not so easy for programmers!! We always want optimal cost.  And you have to find the minimum number of characters required to make a given string to a palindrome if you are allowed to insert characters at any position of the string.
'''
def del_right(word, a, b):
    cnt = 1
    while word[a] != word[b - 1]:
        print(a, b, word[a], word[b])
        b -= 1
        cnt += 1
    return cnt

def del_left(word, a, b):
    cnt = 1
    while word[a + 1] != word[b]:
        print(a, b, word[a], word[b])
        a += 1
        cnt += 1
    return cnt

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        word = input()
        a, b = 0, len(word) - 1
        len_pal = 0
        while a < len(word) // 2:
            if word[a] == word[b]:
                print("a & b equal", a, b, word)
                if a == b:
                    len_pal += 1
                else:
                    len_pal += 2
                a += 1
                b -= 1
                print(len_pal)
            else:
                print("a b not equal", word[a], word[b])
                right = del_right(word, a, b)
                left = del_left(word, a, b)
                print(right, left)
                if right < left:
                    print(a, b, word, left, right)
                    if a == b:
                        len_pal += 1
                    else:
                        len_pal += 2
                    a += left
                elif right > left:
                    print(a, b, word, left, right)
                    if a == b:
                        len_pal += 1
                    else:
                        len_pal += 2
                    b -= right
                else:
                    print(a, b, word, left, right)
                    a += left
                    b -= right
                print(len_pal)
        print(a, b)
        if b == a:
            len_pal += 1
        print(len_pal)

