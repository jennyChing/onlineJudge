'''

Palindrome

11151 - Longest Palindrome

For each input string, your program should print the length of the longest palindrome you can get by removing zero or more characters from it.
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

