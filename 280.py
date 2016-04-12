'''
280 - Vertex
(Graph - traversal)
The input data for this program consists of several directed graphs and starting nodes.

For each graph, there is first one line containing a single integer n. This is the number of vertices in the graph.

Following, there will be a group of lines, each containing a set of integers. The group is terminated by a line which contains only the integer 0. Each set represent a collection of edges. The first integer in the set, i, is the starting vertex, while the next group of integers,  tex2html_wrap_inline73 , define the series of edges i ->  tex2html_wrap_inline77 -> k, and the last integer on the line is always 0. Each possible start vertex i,  tex2html_wrap_inline83 will appear once or not at all. Following each graph definition, there will be a one line containing list of integers. The first integer on the line will specify how many integers follow. Each of the following integers represents a start vertex to be investigated by your program. The next graph then follows. If there are no more graphs, the next line of the file will contain only the integer 0.
'''
if __name__ == "__main__":
    while True:
        try:
            # number of vertices in the graph: N
            N = int(input())
            if N == 0:
                break
            # use adjacency matrix to store the graph
            adj_matrix = [ [ False for i in range(N) ] for j in range(N) ]
            # a group of lines, each containing a set of integers
            while True:
                nodes = list(map(int, input().split()))
                if nodes == [0]:
                    break
                for i in range(1, len(nodes) - 1):
                    adj_matrix[nodes[0] - 1][nodes[i] - 1] = True
            # read input as graph lines until reach line contains only 0 to read the requested investigation, each of the following integers represents a start vertex to be investigated by your program
            for k in range(N):
                for i in range(N):
                    if adj_matrix[i][k] == True:
                        for j in range(N):
                            if adj_matrix[k][j] == True:
                                adj_matrix[i][j] = True

            inv = list(map(int, input().split()))[1:]
            # fill in edges to the adjacency matrix
            for n in inv:
                inacess = [i + 1 for i in range(len(adj_matrix[n - 1])) if adj_matrix[n - 1][i] == False]
                print(len(inacess), end = " ")
                for i in inacess:
                    print(i, end = " ")
                    if i == inacess[-1]:
                        print()
        except(EOFError):
            break
