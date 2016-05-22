'''
Permutations - lexicographic order

941 - Permutations

Given a string S (with up to 20 characters, all lowercase letters) and a integer N (0 ≤ N < 20!) find the (N + 1)-th smallest element of the permutation of S (consider the lexicographic order; the permutation of ‘abc’ above, for example, is represented in lexicographic order form left to right).
E.g., if S = “abc” and N = 0, then the result would be “abc”
E.g., if S = “abc” and N = 5, then the result would be “cba”
E.g., if S = “abc” and N = 3, then the result would be “bca”
E.g., if S = “cba” and N = 3, then the result would be “bca”
Notice that the string may not be initially sorted (check the last two examples).
'''
import math

def divide(N, len_S):
    if len_S < 1:
        return k_list
    temp = math.factorial(len_S - 1)
    k, remain = N // temp, N % temp
    k_list.append(k)
    divide(remain, len_S - 1)

if __name__ == '__main__':
    while True:
        try:
            c = int(input())
            for _ in range(c):
                S = sorted(input())
                N = int(input())
                k_list = []
                divide(N, len(S))
                for i in k_list:
                    print(S[i], sep = "", end = "")
                    S.remove(S[i])
                print()

        except(EOFError):
            break
