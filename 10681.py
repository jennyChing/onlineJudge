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
        links = {}
        trav = set()
        for _ in range(L):
            c1, c2 = list(map(int, input().split()))
            if c1 not in links:
                links[c1] = set()
            links[c1].add(c2)
            if c2 not in links:
                links[c2] = set()
            links[c2].add(c1)
        print(links)
        S, E, D = list(map(int, input().split()))
        print(DFS(S, E, D, links, trav))
        print(trav)
        empty = input()

