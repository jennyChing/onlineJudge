'''
10405 - Longest Common Subsequence:
For example, the longest common subsequence of the following two sequences ‘abcdgh’ ans ‘aedfhr’ is ‘adh’ of length 3.
'''
def max_sub(a, b, s, l, com):
    print("start:", a, b, s, l)
    for i in range(l, len(b)):
        if a[s] == b[i]:
            print(a[s], b[i])
            com += 1
            s += 1
            l = i + 1
            print(a, b, s, l)
            if s < len(a) and l < len(b):
                return max_sub(a, b, s, l, com)
        else:
            s += 1
            if s < len(a):
                print(a, b, s, l)
                return max_sub(a, b, s, l, com)

    return com



if __name__ == '__main__':
    while True:
        try:
            for i in range(2):
                a = list(input())
                b = list(input())
                com = 0
                if len(a) < len(b):
                    print(max_sub(a, b, 0, 0, com))
                else:
                    print(max_sub(b, a, 0, 0, com))
        except(EOFError):
            break
