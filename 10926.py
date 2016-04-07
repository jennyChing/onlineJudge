'''
Graph problem - Traversal
10926 - How Many Dependencies?
In this problem you will need to find out which task has the most number of dependencies. A task A depends on another task B if B is a direct or indirect dependency of A.  For example, if A depends on B and B depends on C, then A has two dependencies, one direct and one indirect.
'''
def DFS(nodes, i, trav):
    if i not in trav:
        trav.add(i)
        for j in nodes[i]:
            DFS(nodes, j, trav)

if __name__ == '__main__':
    while True:
        try:
            N = int(input())
            if N == 0:
                break
            nodes = {}
            for i in range(1, N + 1):
                node = list(map(int, input().split()))
                nodes[i] = node[1:]
            max_cnt = 0
            max_node = 0
            for i in range(1, N + 1):
                trav = set()
                DFS(nodes, i, trav)
                if max_cnt < len(trav):
                    max_cnt, max_node = len(trav), i
            print(max_node)
        except(EOFError):
            break
