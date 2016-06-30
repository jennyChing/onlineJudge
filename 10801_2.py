'''
Shortest Path  找不在樹上、離根最近的點，就直接窮舉 d[] 表格，找出最小的 d[b]

10801 - Lift Hopping

You are on floor 0 and would like to get to floor k as quickly as possible. Assume that you do not need to wait to board the first elevator you step into and (for simplicity) the operation of switching an elevator on some floor always takes exactly a minute. Of course, both elevators have to stop at that floor. Calculate the minimum number of seconds required to get from floor 0 to floor k (passing floor k while inside an elevator that does not stop there does not count as “getting to floor k”).
'''
from heapq import *
#from numpypy import *
from itertools import combinations
INF = 1 << 30


def dijkstra(source):
    dist = [0] * nVertices
    for i in range(nVertices):
        dist[i] = graph[source][i]
    dist[source] = 0
    visited = [0] * nVertices
    heap = []
    for i in range(nVertices):
        heappush(heap, (dist[i], i))
    while heap:
        d1, v1 = heappop(heap)
        if d1 == INF:
            break
        if visited[v1]:
            continue
        dist[v1] = d1
        visited[v1] = 1
        for v2 in range(nVertices):
            value = graph[v1][v2] + d1
            if dist[v2] > value:
                dist[v2] = value
                heappush(heap, (value, v2))
    return dist

while True:
    try:
        n, k = list(map(int, input().split()))
    except:
        break
    elevTime  = list(map(int, input().split()))
    elevators = []
    for i in range(n):
        elevators.append(list(map(int, input().split())))
    vertices = []
    for i in range(n):
        for v in elevators[i]:
            vertices.append((i, v))
    print(elevators, vertices)
    nVertices = len(vertices)
# all default length is infinite, then update the length of floors reachable
    graph = [ [ float('inf') for i in range(nVertices) ] for j in range(nVertices) ]
    for i in range(nVertices):
        for j in range(i + 1, nVertices):
            if vertices[i][0] == vertices[j][0]:
                elev = vertices[i][0]
                graph[i][j] = graph[j][i] =\
                    elevTime[elev] * abs(vertices[i][1] - vertices[j][1])
            if vertices[i][1] == vertices[j][1]:
                if vertices[i][1] == 0:
                    graph[i][j] = graph[j][i] = 0
                else:
                    graph[i][j] = graph[j][i] = 60
    print(graph)
    source = -1
    for i, v in enumerate(vertices):
        if v[1] == 0:
            source = i
            break
    dist = dijkstra(source)
    minDist = INF
    for i in range(nVertices):
        if vertices[i][1] == k:
            minDist = min(minDist, dist[i])
    if minDist == INF:
        print ('IMPOSSIBLE')
    else:
        print (int(minDist))


