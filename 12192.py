'''
SequenceManipulation - Search in Sorted Matrix: Saddleback Search
12192 - Grapevine

You must write a program that, given the description of the rectangular area of interest in the mountain, and a list of queries containing height intervals, determines, for each query, the largest side, in number of properties, of a contiguous square area with heights within the specified interval.

Input
The input contains several test cases. The first line of a test case contains two integers N and M, separated by a single space, representing respectively the number of properties in the North-South direction (1 ≤ N ≤ 500) and the number of properties in the West-East direction (1 ≤ M ≤ 500) of the region of interest. Each of the next N lines contains M integers Hi,j , separated by single spaces, indicating the heights of the properties in the region of interest (0 ≤ Hi,j ≤ 105 , for 1 ≤ i ≤ N and 1 ≤ j ≤ M; also, Hi−1,j ≤ Hi,j and Hi,j−1 ≤ Hi,j ). The next line contains an integer Q indicating the number of queries (1 ≤ Q ≤ 104). Each of the next Q lines describes a query, and contains two integers L and U, separated by a single space, indicating one interval of heights (0 ≤ L ≤ U ≤ 105).  The heights of properties to be rented must be greater than or equal to L and less than or equal to U.  The last test case is followed by a line containing two zeros separated by a single space.

Output
For each test case in the input your program must print Q + 1 lines. Each of the first Q lines must contain a single integer, indicating the largest side, in number of properties, of a contiguous square area with heights within the interval specified in the respective input query. The last line to be printed for each test case is used as a separator and must contain a single character ‘-’ (known as hyphen or minus sign).

Sample Input
4 5 # M x N field
13 21 25 33 34
16 21 33 35 35
16 33 33 45 50
23 51 66 83 93
3  # number of queries
22 90 # interval of query one
33 35
20 100

Sample Output
3 # the max square that all elements are within the interval
2
4
-
'''
def largeSmallest(lst, n):
    print(lst, n)
    l, r = 0, len(lst) - 1
    temp = None
    while r >= l:
        m = (l + r) // 2
        if n > lst[m]:
            l = m + 1
        else:
            temp = m
            r = m - 1
    return temp

def smallLargest (lst, n):
    l, r = 0, len(lst) - 1
    temp = None
    while r >= l:
        m = (l + r) // 2
        if n < lst[m]:
            r = m - 1
        else:
            temp = m
            l = m + 1
    return temp

if __name__ == '__main__':
    while True:
        try:
            N_M = list(map(int, input().split()))
            N, M = N_M[0], N_M[1]
            if N and M == 0:
                break
            field = [ [] for i in range(N) ]
            for i in range(N):
                ms = list(map(int, input().split()))
                field[i] = ms
            queries = int(input())
            for _ in range(queries):
                interval = list(map(int, input().split()))
                small, big = interval[0], interval[1]
                print("Query", small, big)
                l, r, u, d = 0, 0, float('inf'), 0
                i, j = 0, 0
# find the top line that works for the range
                while i < N - 1:
                    a, b = smallLargest(field[i], small), smallLargest(field[i], big)

                    if a != None and a >= l:
                        l = a
                    if b != None and b >= r:
                        r = b
                    if i < u:
                        u = i
                    if i > d:
                        d = i
                    if (a and b != None):
                        i += 1
                    else:
                        i += 1
                print("u/d/l/r", min(d - u + 1, r - l + 1), d - u, r - l)
            print("-")
        except(EOFError):
            break

