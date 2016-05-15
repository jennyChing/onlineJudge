'''
Tree diameter - use adjacency matrix

10308 - Roads in the North

Input
The input contains several sets of input. Each set of input is a sequence of lines, each containing three positive integers: the number of a village, the number of a different village, and the length of the road segment connecting the villages in kilometers. All road segments are two-way. Two consecutive sets are separated by a blank line.

Output
For each set of input, you are to output a single line containing a single integer: the road distance between the two most remote villages in the area.
'''
v_list = {}


def DFS(x, px, v_list, dia, trav): # px is the father of p
    h1, h2 = 0, 0 # record the first and second height of the subtree under the current node
    for y in range(len(v_list)):
        if x in v_list and y != px and y in v_list[x] and y not in trav:
            h = DFS(y, x, v_list, DFS(y, x, v_list, dia, trav)[1], trav)[0] + v_list[y][x]
            trav.add(x)
            print("Here", x, v_list[x], px, y, v_list[y])
            if h > h1:
                h2, h1 = h1, h
            elif h > h2:
                h2 = h
        dia = max(dia, h1 + h2)
    return h1, dia


def diameter(v_list):
    dia = 0
    trav = set()
    root = 6  # every node in a tree can be the root
    return DFS(root, root, v_list, dia, trav)

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
