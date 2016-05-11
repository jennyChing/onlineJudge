'''
Tree diameter - use adjacency matrix

10308 - Roads in the North

Input
The input contains several sets of input. Each set of input is a sequence of lines, each containing three positive integers: the number of a village, the number of a different village, and the length of the road segment connecting the villages in kilometers. All road segments are two-way. Two consecutive sets are separated by a blank line.

Output
For each set of input, you are to output a single line containing a single integer: the road distance between the two most remote villages in the area.
'''
dia = 0
v_list = []
v_len = 0

def adj(v_list):
    v_adj = [ [ 0 for i in range(v_len) ] for j in range(v_len)]
    for v in v_list:
        v_adj[v[0] - 1][v[1] - 1] = v[2]
        v_adj[v[1] - 1][v[0] - 1] = v[2]
    return v_adj

def DFS(root, v_adj):
    h1, h2 = 0, 0 # record the first and second height
    for y in range(len(v_adj)):
        if v_adj[x][y] != 0:
            h = DFS(y, x, v_list) + 1
            if h > h1:
                h2, h1 = h1, h
            elif h > h2:
                h2 = h
    dia = max(dia, h1 + h2) # pass through root's first and second longest
    return h1


def diameter(v_list):
    v_adj = adj(v_list) # turn the adjacency list into matrix
    root = 0
    return DFS(root, root, v_adj)



if __name__ == '__main__':
    while True:
        try:
            v = list(map(int, input().split()))
            if len(v) == 0:
                print(diameter(v_list))
                v_list = []
            else:
                print(v)
                v_len = max(v[0], v[1], v_len)
                v_list.append(v)
        except(EOFError):
            print(diameter(v_list))
            break
