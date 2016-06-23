'''
Topological Sort

200 - Rare Order

You are to write a program to complete the collector’s work. In particular, your program will take a set of strings that has been sorted according to a particular collating sequence and determine what that sequence is.

Sample Input
XWY
ZX
ZXY
ZXW
YWWX
#
Sample Output => the new letter order that the input is based on
XZYW
'''
from collections import defaultdict
from collections import deque

def topoSort(graph):
    def topoVisit(u):
        visited[u] = 1
        for v in graph[u]:
            if visited[v] == 0:
                topoVisit(v)
        topoSorted.appendleft(u)
    visited = {}
    for v in graph:
        visited[v] = 0
    topoSorted = deque()
    for v in graph:
        if visited[v] == 0:
            topoVisit(v)
    return topoSorted

if __name__ == '__main__':
    words = []
    while True:
        w = input()
        if w == '#':
            break
        words.append(w)
    st = {}
    for i in range(1, len(words)):
        s1 = words[i - 1]
        s2 = words[i]
        for j in range(min(len(s1), len(s2))): # compare the words in order
            if s1[j] != s2[j]:
                if s1[j] not in st:
                    st[s1[j]]= []
                if s2[j] not in st:
                    st[s2[j]]= []
                st[s1[j]].append(s2[j])
                break
    print(''.join(topoSort(st)))
