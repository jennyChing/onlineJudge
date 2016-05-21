'''
tree - radius (balanced height)

10459 - The Tree Root

Input
Each dataset starts with a positive integer N (3 ≤ N ≤ 5000), which is the number of nodes in the tree. Each node in the tree has a unique id from 1 to N. Then successively for each i’th node there will be a positive integer K[i] following id of K[i] nodes which are adjacent to i. Input is terminated by EOF.

Output
For each dataset print two lines. In the 1st line show all the best roots in ascending order and in next
line show all worst roots in ascending order. See sample output for exact format.
'''
def DFS(x, px):
# y is the node number and x is the index number (y = x + 1)
    for y in tree[x]:
        if y != px  and y in tree[x]:
            depth[y - 1] = depth[x] + 1
            DFS(y - 1, x + 1)


if __name__ == '__main__':
    while True:
        try:
            tree = []
# store the tree as array mapped by index instead of storing as dictionary
            N = input()
            while len(N) == 0:
                N = input()
            N = int(N)
            for i in range(N):
                node = list(map(int, input().split()))
                tree.append(node[1:])
            min_def, max_def = float('inf'), 0
            depth_all = [] * N
            for j in range(N):
                depth = [1] * N
                DFS(j, j + 1)
                depth_all.append(depth)
                min_def = min(max(depth), min_def)
                max_def = max(max(depth), max_def)
            best_root, worst_root = [], []
            for k in range(N):
                if max(depth_all[k]) == max_def:
                    worst_root.append(k + 1)
                elif max(depth_all[k]) == min_def:
                    best_root.append(k + 1)
            print("Best Roots  :", end = "")
            for i in best_root:
                print('', i, end = "")
            print()
            print("Worst Roots :", end = "")
            for i in worst_root:
                print('', i, end = "")
            print()

        except(EOFError):
            break
