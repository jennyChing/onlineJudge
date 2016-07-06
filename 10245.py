'''
Sweep Line

10245 - The Closest Pair Problem

Input
The input file contains several sets of input. Each set of input starts with an integer N(0 ≤ N ≤ 10000), which denotes the number of points in this set. The next N line contains the coordinates of N twodimensional points. The first of the two numbers denotes the X-coordinate and the latter denotes the Y -coordinate. The input is terminated by a set whose N = 0. This set should not be processed. The value of the coordinates will be less than 40000 and non-negative.

Output
For each set of input produce a single line of output containing a floating point number (with four digits after the decimal point) which denotes the distance between the closest two points. If there is no such two points in the input whose distance is less than 10000, print the line ‘INFINITY’
'''
if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            if n == 0:
                break
            for _ in range(n):
                coor = list(map(int, input().split()))
        except(EOFError):
            break

