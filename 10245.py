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
            coor = []
            for _ in range(n):
                c = list(map(int, input().split()))
                coor.append((c[0], c[1]))
                coor = sorted(coor)
            pairs = []
            for i in range(len(coor) - 1):
                l = coor[i]
                dist = float('inf')
                for j in range(i + 1, len(coor)):
                    d = (coor[j][0] - coor[i][0])**2 + (coor[j][1] - coor[i][1])**2
                    if d**.5 < dist:
                        dist = d**.5
                pairs.append(dist)
            pairs = sorted(pairs)
            if len(pairs) > 0:
                if pairs[0] > 1000:
                    print('INFINITY')
                else:
                    print("{0:.4f}".format(pairs[0]))
            else:
                print('INFINITY')
        except(EOFError):
            break

