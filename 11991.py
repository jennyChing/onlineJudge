'''
Data - [array]
11991 - Easy Problem from Rujia Liu?
Given an array, your task is to find the k-th occurrence (from left to right) of an integer v. To make the problem more difficult (and interesting!), you’ll have to answer m such queries.

Input

There are several test cases. The first line of each test case contains two integers n, m (1 ≤ n, m ≤ 100, 000), the number of elements in the array, and the number of queries. The next line contains n positive integers not larger than 1,000,000. Each of the following m lines contains two integer k and v (1 ≤ k ≤ n, 1 ≤ v ≤ 1, 000, 000). The input is terminated by end-of-file (EOF).

Output

For each query, print the 1-based location of the occurrence. If there is no such element, output ‘0’ instead.
'''
if __name__ == '__main__':
    while True:
        try:
            n_m = list(map(int, input().split()))
            m = n_m[1]
            nums = list(map(int, input().split()))
            memo = {}
            for i in range(len(nums)):
                if nums[i] in memo:
                    memo[nums[i]].append(i + 1)
                else:
                    memo[nums[i]] = [i + 1]
            for i in range(m):
                k_v = list(map(int, input().split()))
                k, v = k_v[0], k_v[1]
                if v in memo:
                    if k <= len(memo[v]):
                        print(memo[v][k - 1])
                    else:
                        print(0)
                else:
                    print(0)
        except(EOFError):
            break
