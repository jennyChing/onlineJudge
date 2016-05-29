'''
環狀排列 Permutations

11255 - Necklace

Input
The input begins with an integer N (≤ 2500) which indicates the number of test cases followed. Each of the following test cases consists of three non-negative integers a, b, c, where 3 ≤ a + b + c ≤ 40.

Output
For each test case, print out the number of different necklaces that formed by a white pearls, b grey
pearls and c black pearls in a single line.
'''
import math
if __name__ == '__main__':
    case = int(input())
    for _ in case:
        a, b, c = list(map(int, input().split()))
        ans = math.factorial(a - 1)
        print(ans)

