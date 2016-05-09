'''
Binary search tree recording binary numbers

712 - S-Trees

A Strange Tree (S-tree) over the variable set Xn = {x1, x2, . . . , xn} is a binary tree representing a Boolean function f : {0, 1} n → {0, 1}. Each path of the S-tree begins at the root node and consists of n + 1 nodes. Each of the S-tree’s nodes has a depth, which is the amount of nodes between itself and the root (so the root has depth 0). The nodes with depth less than n are called non-terminal nodes. All non-terminal nodes have two children: the right child and the left child. Each non-terminal node is marked with some variable xi from the variable set Xn. All non-terminal nodes with the same depth are marked with the same variable, and non-terminal nodes with different depth are marked with different variables.
The nodes having depth n are called terminal nodes. They have no children and are marked with either 0 or 1. Note that the variable ordering and the distribution of 0’s and 1’s on terminal nodes are sufficient to completely describe an S-tree.
'''
tree = 0
if __name__ == '__main__':
    while True:
        try:
            depth = int(input())
            if depth == 0:
                break
            tree += 1
            print("S-Tree #", tree, ":", sep = "")
            order = list(map(str, input().split()))
            order_list = []
            for o in order:
                order_list.append(int(o[1]))
            nodes = input()
            m = int(input())
            for _ in range(m):
                temp = nodes
                v = input()
                for b in order_list:
                    if v[b - 1] == '0':
                        temp = temp[:len(temp)//2]
                    else:
                        temp = temp[len(temp)//2:]
                print(temp, end = "")
            print()
            print()
        except(EOFError):
            break
