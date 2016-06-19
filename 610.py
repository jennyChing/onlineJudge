'''
Oriented Graph

610 - Street Directions

Input
The input consists of a number of cases. The first line of each case contains two integers n and m. The number of intersections is n (2 ≤ n ≤ 1000), and the number of streets is m. The next m lines contain the intersections incident to each of the m streets. The intersections are numbered from 1 to n, and each street is listed once. If the pair i j is present, j i will not be present. End of input is indicated by n = m = 0.

Output
For each case, print the case number (starting from 1) followed by a blank line. Next, print on separate lines each street as the pair i j to indicate that the street has been assigned the direction going from intersection i to intersection j. For a street that cannot be converted into a one-way street, print both i j and j i on two different lines. The list of streets can be printed in any order. Terminate each case with a line containing a single ‘#’ character.  Note: There may be many possible direction assignments satisfying the requirements. Any such assignment is acceptable.
'''
cases = 0
if __name__ == '__main__':
    while True:
        n, m = list(map(int, input().split()))
        if n == 0 and m == 0:
            break
        cases += 1
        for _ in range(m):
            i, j = list(map(int, input().split()))

1 2
1 3
2 4
3 4
4 5
4 6
5 7
6 7
2 5
3 6


1 2
2 4
3 1
3 6
4 3
5 2
5 4
6 4
6 7
7 5


