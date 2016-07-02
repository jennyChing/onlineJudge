'''
Path

10356 - Rough Roads

Input
The first line of each test case contains two integers: n (the number of junctions, 1 < n < 501) and r (the number of bi-directional roads connecting these junctions). The junctions are numbered with 0, 1, . . . , n − 1. The gate of the village and the grandfather’s house is situated at junctions 0 and n − 1 respectively. Each of the next r lines (one for each road) contains three non-negative integers: two junction-numbers that the corresponding road connects and the length of the road in kilometers. A road always connects two different junctions. Length of a road is not more than 20km and not less than 1km.

Output
For each dataset, print the set number (1, 2, . . .) in a line followed by the length of the shortest path.  However, if it is not possible to reach there in the specified way, print a ‘?’
'''
from heapq import *
from itertools import combinations
INF = 1 << 30

def dijkstra(source):
# dist stores the updated length of the shortest path from source to current node
    dist = [0] * n
    for i in range(n):
        dist[i] = graph[source][i]
    dist[source] = 0
    visited = [0] * n
    heap = []
    for i in range(n):
        heappush(heap, (dist[i], i))
    while heap:
        print(heap)
        d1, v1 = heappop(heap)
        if d1 == INF:
            break
        if visited[v1]:
            continue
        dist[v1] = d1
        for v2 in range(n):
            value = graph[v1][v2] + d1
            if dist[v2] > value:
                dist[v2] = value
                heappush(heap, (value, v2))
    return dist

if __name__ == '__main__':
    while True:
        try:
            n, r = list(map(int, input().split()))
            graph = [[ float('inf') for i in range(n) ] for j in range(n) ]
            for _ in range(r):
                road = list(map(int, input().split()))
                graph[road[0]][road[1]] = road[2]
                graph[road[1]][road[0]] = road[2]
            print(graph)
            dist = dijkstra(0)
            print(dist)
            minDist = INF

        except(EOFError):
            break


