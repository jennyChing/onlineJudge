'''
Topological Ordering

124 - Following Orders

The Input

The input consists of a sequence of constraint specifications. A specification consists of two lines: a list of variables on one line followed by a list of constraints on the next line. A constraint is given by a pair of variables, where x y indicates that x < y.

The Output

For each constraint specification, all orderings consistent with the constraints should be printed. Orderings are printed in lexicographical (alphabetical) order, one per line.
Output for different constraint specifications is separated by a blank line.
'''

if __name__ == '__main__':
    while True:
        try:
            char = sorted(list(map(str, input().split())))
            constrain = list(map(str, input().split()))
        except(EOFError):
            break
        MAXN = 26

# use a graph to store the eligible paths
        graph = [[ 0 for x in range(MAXN)] for y in range(MAXN)]
        nodes = [ord(c) - ord('a') for c in char]
        nodes.sort()
        N = len(constrain) // 2
        for i in range(N):
            graph[ord(constrain[i * 2 + 1]) - ord('a')][ord(constrain[i * 2]) - ord('a')] = 1
# use kij algorithm to compute the reachability of all constraints
        for k in range(MAXN):
            for i in range(MAXN):
                for j in range(MAXN):
                    graph[i][j] |= (graph[i][k] & graph[k][j])
        N = len(nodes)
        path = []
        used = [False] * N

# use DFS to traverse the graph and print whenever the len of nodes is reached(setp = N)
        def perm(step):
            if step == N:
                print (''.join(chr(p + ord('a')) for p in path))
                return
            for i in range(N):
# used[i] is False (node[i] is not used) and there is no contrains from node[i] to the rest of the path
                if not used[i] and (step == 0 or all([graph[p][nodes[i]] == 0 for p in path])):
                    path.append(nodes[i])
                    used[i] = True
                    perm(step + 1)
                    path.pop()
                    used[i] = False
        perm(0)
        print()



