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
Solution:
 go through each line in field[i], and locate one left and one right in each line. Every pair of left and right can form a square, find the largest square and print the value
 for every upper-left, check if their lower-right is illigible. If not, length - 1 and check again the lower-right
'''
def largeSmallest(lst, target):
    l, r = 0, len(lst) - 1
    temp = None
    while r >= l:
        m = (l + r) // 2
        if target > lst[m]:
            l = m + 1
        else:
            temp = m
            r = m - 1
    return temp

def smallLargest (lst, target):
    l, r = 0, len(lst) - 1
    temp = None
    while r >= l:
        m = (l + r) // 2
        if target < lst[m]:
            r = m - 1
        else:
            temp = m
            l = m + 1
    return temp

if __name__ == '__main__':
    while True:
        try:
            N, M = list(map(int, input().split()))
            if N and M == 0:
                break
            field = [ [] for i in range(N) ]
            for i in range(N):
                field[i] = list(map(int, input().split()))
            queries = int(input())
            for _ in range(queries):
                small, big = list(map(int, input().split()))
                print("Query", small, big)
                i = 0
# find the top line that works for the range
                left = {}
                right = {}
                while i < N:
                    a, b = largeSmallest(field[i], small), smallLargest(field[i], big)
                    if a != None and field[i][a] <= big:
                        left[i] = a
                    if b != None and field[i][b] >= small:
                        right[i] = b
                    i += 1
                max_g = 0
                for k in range(len(left)):
                    for h in range(len(right)):
                        max_g = max(max_g, (right[h] - left[k]) * (h - k))
                print(left, right, max_g)
            print("-")
        except(EOFError):
            break

