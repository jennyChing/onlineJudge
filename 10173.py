'''
Rectangles

10173 - Smallest Bounding Rectangle

Input
The input file may contain multiple test cases. Each test case begins with a line containing a positive integer n (< 1001) indicating the number of points in this test case. Then follows n lines each containing two real numbers giving respectively the x- and y-coordinates of a point. The input terminates with a test case containing a value 0 for n which must not be processed.

Output
For each test case in the input print a line containing the area of the smallest bounding rectangle rounded to the 4th digit after the decimal point.
'''
if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break
        x = []
        y = []
        for _ in range(n):
            point = list(map(float, input().split()))
            x.append(point[0])
            y.append(point[1])
        max_x = max(x)
        max_y = max(y)
        min_x = min(x)
        min_y = min(y)
        print("{0:0.4f}".format((max_x - min_x) * (max_y - min_y)))

