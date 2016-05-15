'''
Tree diameter - use adjacency matrix

10308 - Roads in the North

Input
The input contains several sets of input. Each set of input is a sequence of lines, each containing three positive integers: the number of a village, the number of a different village, and the length of the road segment connecting the villages in kilometers. All road segments are two-way. Two consecutive sets are separated by a blank line.

Output
For each set of input, you are to output a single line containing a single integer: the road distance between the two most remote villages in the area.
'''
v_list = {}

def DFS(x, px): # px is the father of p
    h1, h2, dia = 0, 0, 0 # record the first and second height of the subtree under the current node
    for y, v in v_list[x].items():
        if y != px and y in v_list[x]:
            h, c_dia = DFS(y, x) # c_dia is the local diaometer that doesn't pass me
            h = h + v_list[x][y]
# find the highest 2 routes in subtree
            if h > h1:
                h2, h1 = h1, h
            elif h > h2:
                h2 = h
            dia = max(dia, c_dia) # global dia and local c_dia
    dia = max(dia, h1 + h2) # dia stored in the outtest DFS recursive function
    return h1, dia

def diameter(v_list):
    root = 1
    return DFS(root, root)

if __name__ == '__main__':
    while True:
        try:
            v = list(map(int, input().split()))
            if len(v) == 0:
                print(diameter(v_list)[1])
                v_list = {}
            else:
                if v[0] not in v_list:
                    v_list[v[0]] = {v[1] : v[2]}
                else:
                    v_list[v[0]][v[1]] = v[2]
                if v[1] not in v_list:
                    v_list[v[1]] = {v[0] : v[2]}
                else:
                    v_list[v[1]][v[0]] = v[2]
        except(EOFError):
            print(diameter(v_list)[1])
            break
