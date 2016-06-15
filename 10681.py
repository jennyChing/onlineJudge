'''
Reachability

Input
The input file contains several input sets. The description of each set is given below: Each set starts with two integers C (0 < C ≤ 100), the number of cities, and L (0 ≤ L ≤ 500), the number of links between the cities. Follow L lines, where each line has two numbers: A and B (1 ≤ A, B ≤ C), meaning there is a link between these two cities. You can assume that A and B are different numbers. After the L lines, there are three integers: S, E and D. Where S is the city where the trip must start, E is the city where the trip must end, and D (0 ≤ D ≤ 200) is the maximum number of days for Teobaldo to go from S to E.  Input is terminated by a set where C = L = 0. This set should not be processed. There is a blank line beteween two input sets.

Output
    For each input set produce one line of output, indicating if Teobaldo can travel how he wishes. See the examples below for the exact input/output format.
'''
def DFS(start, end, days, links, trav):
    if start not in trav and start != end:
        print(start, trav)
        trav.add(start)
        for n in links[start]:
            print('n', n, end, len(trav), trav)
            if n != end:
                DFS(n, end, days, links, trav)
            elif n == end and len(trav) == days:
                trav.add(end)
                return True
    return False

if __name__ == '__main__':
    while True:
        C, L = list(map(int, input().split()))
        if C == 0 and L == 0:
            break
# store graph in a adj matrix
        graph =  [[ 0 for i in range(C + 1) ] for j in range(C + 1)]
        for _ in range(L):
            c1, c2 = list(map(int, input().split()))
            graph[c1][c2] = 1
            graph[c2][c1] = 1
        S, E, D = list(map(int, input().split()))
# use dynamic programming to store the cities traveled and see if the trip can start from S to E
        dp = [[ 0 for i in range(D + 1) ] for j in range(C + 1)]
# initial the traversal from S start and apply the ijk reachability algorithm
        dp[S][0] = 1
        for d in range(1, D + 1):
            for c in range(1, C + 1):
                for c1 in range(1, C + 1):
                    if c1 != c and dp[c1][d - 1] and graph[c1][c]:
                        dp[c][d] = 1
                        break
# see if the dp records traversal results that E end is reached
        if dp[E][D] == 1:
            print('Yes, Teobaldo can travel.')
        else:
            print('No, Teobaldo can not travel.')
        empty = input()

