'''
Palindrome

10739 - String to Palindrome

6 ways:
    s[i] replace s[j] => F(i + 1, j - 1)
    s[j] replace s[i] => F(i + 1, j - 1)
    delete s[i] or add i after j => F(i, j - 1)
    delete s[j] or add j after i => F(i + 1, j)
boundary case:
    Assuming i >= j, it means no need to change since substring s[i:j] is either one character or empty string.  So we return 0.
'''
def DP(left, right):
    if table[left][right] == -1:
        if left >= right:
            table[left][right] = 0
        elif buff[left] == buff[right]:
            table[left][right] = DP(left + 1, right - 1)
        else:
            table[left][right] = 1 + min(DP(left + 1, right - 1), DP(left + 1, right), DP(left, right - 1))
    return table[left][right]

cases = 0
if __name__ == '__main__':
    case = int(input())
    for _ in range(case):
        cases += 1
        buff = input()
        table = [ [ -1 for i in range(len(buff)) ] for j in range(len(buff)) ]
        print("Case ", cases, ": ", DP(0, len(buff) - 1), sep = '')


