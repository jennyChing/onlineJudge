'''

Reachability

10720 - Graph Construction

Graph is a collection of edges E and vertices V. Graph has a wide variety of applications in computer.  There are different ways to represent graph in computer. It can be represented by adjacency matrix or by adjacency list. There are some other ways to represent graph. One of them is to write the degrees (the numbers of edges that a vertex has) of each vertex. If there are n vertices then n integers can represent that graph. In this problem we are talking about simple graph which does not have same endpoints for more than one edge, and also does not have edges with the same endpoint.  Any graph can be represented by n number of integers. But the reverse is not always true. If you are given n integers, you have to find out whether this n numbers can represent the degrees of n vertices of a graph.
'''
if __name__ == '__main__':
    while True:
        graph = list(map(int, input().split()))
        if graph == [0]:
            break
        n = graph[0]
        degrees = graph[1:]
        isPoss = True
        if sum(degrees) % 2 == 1:
            isPoss = False
        sorted_d = sorted(degrees, reverse=True)
        if sorted_d[0] > n:
            isPoss = False
        else:
            while sum(sorted_d) > 0 and len(sorted_d) > sorted_d[0]:
                for i in range(sorted_d[0]):
                    if sorted_d[i + 1] == 0:
                        isPoss = False
                        break
                    sorted_d[i + 1] -= 1
                sorted_d.pop(0)
        if isPoss == False:
            print("Not possible")
        else:
            print("Possible")



