'''
Backtracking

140 - Bandwidth

Given a graph (V,E) where V is a set of nodes and E is a set of arcs in VxV, and an ordering on the elements in V, then the bandwidth of a node v is defined as the maximum distance in the ordering between v and any node to which it is connected in the graph. The bandwidth of the ordering is then defined as the maximum of the individual bandwidths

在當前給定的排序中，與v距離最遠的且與v有邊相連的頂點與v的距離。給定排序的帶寬定義為各頂點帶寬的最大值
給定n個節點，（n<=8），節點的編號為A～Z來表示，要求找到一個節點的序列，使得該序列最大的節點的Bandwidth為所有序列中的最小值，（節點的Bandwidth是指和它所連接的點中和它距離最大的值）
'''
from itertools import permutations
if __name__ == '__main__':
    while True:
        graph = list(map(str, input().split(';')))
        if graph == ['#']:
            break
        v = {}
        node = set()
        for i in range(len(graph)):
            v[graph[i][0]] = graph[i][2:]
            node.add(graph[i][0])
            for j in graph[i][2:]:
                node.add(j)
        node = sorted(node)
        perms = list(permutations(node))
        max_band = 0
        for p in perms:
            for n in p:





