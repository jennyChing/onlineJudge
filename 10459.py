'''
tree - radius (balanced height)

10459 - The Tree Root

Input
Each dataset starts with a positive integer N (3 ≤ N ≤ 5000), which is the number of nodes in the tree. Each node in the tree has a unique id from 1 to N. Then successively for each i’th node there will be a positive integer K[i] following id of K[i] nodes which are adjacent to i. Input is terminated by EOF.

Output
For each dataset print two lines. In the 1st line show all the best roots in ascending order and in next
line show all worst roots in ascending order. See sample output for exact format.
'''
def DFS(tree, p, px, h):
    print(h, tree[p], tree[tree[p]], p, px)
    if p in tree and px != tree[p]:
        h += 1
        DFS(tree, tree[p], tree[tree[p]], h)
        print(h, tree[p], tree[tree[p]])
    return h

if __name__ == '__main__':
    while True:
        try:
            tree = {}
            h = 0
            N = int(input())
            for i in range(N):
                node = list(map(int, input().split()))
                for j in range(1, len(node)):
                    tree[i + 1] = node[j]
            root = 2
            print(DFS(tree, root, root, h))
        except(EOFError):
            break
