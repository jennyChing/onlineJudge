'''
Topological Ordering

10305 - Ordering Tasks

Input
The input will consist of several instances of the problem. Each instance begins with a line containing two integers, 1 ≤ n ≤ 100 and m. n is the number of tasks (numbered from 1 to n) and m is the number of direct precedence relations between tasks. After this, there will be m lines with two integers i and j, representing the fact that task i must be executed before task j.  An instance with n = m = 0 will finish the input.

Output
For each instance, print a line with n integers representing the tasks in a possible order of execution.
'''
from collections import defaultdict

def topoSort(nodes, graph):
    visited = {}
    result = []
    # this vector stores topological sort in reverse order
    for v in nodes:
        visited[v] = 0

    # visit the node u and visit the nodes related to node u
    def topoVisit(u):
        visited[u] = 1
        print(visited, graph[u], result)
        for v in graph[u]:
            if not visited[v]:
                topoVisit(v)
                print(result)
        result.append(u)  # this is the only change

    # loop through the nodes and check if it is visited, if not, topoVisit the node
    for v in nodes:
        if not visited[v]:
            topoVisit(v)

    # result is generated from the backtracking method
    result.reverse()
    print(' '.join([str(e) for e in result]))

if __name__ == '__main__':
    while True:
        n, m = list(map(int, input().split()))
        if n == 0 and m == 0:
            break
        graph = defaultdict(list)
        nodes = list(range(1, n + 1))
        for i in range(m):
            v1, v2 = list(map(int, input().split()))
            graph[v1].append(v2)
        print(graph.items())
        topoSort(nodes, graph)
