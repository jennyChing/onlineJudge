'''
Binary Tree

122 - Trees on the level

The Input
The input is a sequence of binary trees specified as described above. Each tree in a sequence consists of several pairs (n,s) as described above separated by whitespace. The last entry in each tree is (). No whitespace appears between left and right parentheses. All nodes contain a positive integer. Every tree in the input will consist of at least one node and no more than 256 nodes. Input is terminated by end-of-file.

The Output
For each completely specified binary tree in the input file, the level order traversal of that tree should be printed. If a tree is not completely specified, i.e., some node in the tree is NOT given a value or a node is given a value more than once, then the string ''not complete'' should be printed.
'''
if __name__ == '__main__':
    while True:
        try:
            tree = list(map(str, input().split()))
            if tree[-1] != '()':
                tree += list(map(str, input().split()))
        except(EOFError):
            break
        tree = tree[:-1]
        tree_dic = {}
        for i in range(len(tree)):
            temp = tree[i].split(',')
            tree_dic[temp[1][:-1]] = temp[0][1:]

        if '' in tree_dic:
            print(tree_dic[''])
        else:
            print("not complete")
        print(tree_dic)
