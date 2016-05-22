'''
Binary Tree

122 - Trees on the level

The Input
The input is a sequence of binary trees specified as described above. Each tree in a sequence consists of several pairs (n,s) as described above separated by whitespace. The last entry in each tree is (). No whitespace appears between left and right parentheses. All nodes contain a positive integer. Every tree in the input will consist of at least one node and no more than 256 nodes. Input is terminated by end-of-file.

The Output
For each completely specified binary tree in the input file, the level order traversal of that tree should be printed. If a tree is not completely specified, i.e., some node in the tree is NOT given a value or a node is given a value more than once, then the string ''not complete'' should be printed. (nodes that are not touched or touched twice in the graph during the traversal by DFS)

Step1. check if it is a tree
Step2. print out the level-order

1. store as tree: if node's val is already assign then it is touched twice; if the tree have nodes remain val as none, the tree is not complete
2. store as a graph to identify whether the case is a compplete tree: traverse all the nodes and see if any node are left out
'''
from collections import deque
class TreeNode (object):
     """tree node for binary tree"""
     def __init__(self, data=None):
         self.data = data
         self.left = self.right = None

if __name__ == '__main__':
    while True:
        try:
            isEnd = False
            tree = list(map(str, input().split()))
            while isEnd == False:
                if tree[-1] != '()':
                    temp = list(map(str, input().split()))
                    tree += temp
                    if tree[-1] == '()':
                        isEnd = True
                    else:
                        isEnd = False
            else:
                isEnd = True
            if isEnd == True:
                tree = tree[:-1]
                tree_dic = {}
                isComplete = True
                for i in range(len(tree)):
                    temp = tree[i].split(',')
                    path, val= temp[1][:-1], temp[0][1:]
                    if path not in tree_dic:
                        tree_dic[path] = val
                    else:
                        isComplete = False
                if '' not in tree_dic:
                    isComplete = False
                root = TreeNode()
                for path, val in tree_dic.items():
                    currNode = root
                    for p in path:
                        if p == 'L':
# if left child already exists then move the path down to the left child
                            if currNode.left:
                                currNode = currNode.left
# but if left child doesn't exists, create a new node with TreeNode and move down left
                            else:
                                currNode.left = TreeNode()
                                currNode = currNode.left
# if right child already exists then move the path down to the right child
                        elif p == 'R':
                            if currNode.right:
                                currNode = currNode.right
# but if right child doesn't exists, create a new node with TreeNode and move down right
                            else:
                                currNode.right = TreeNode()
                                currNode = currNode.right
# assign the value to the current node
                    currNode.data = val
                result = []
# create the deque objects to operate the levels
                currLevel = deque([root])
                nextLevel = deque()
                while currLevel:
                    e = currLevel.popleft()
                    if e.data:
                        result.append(e.data)
                        if e.left:
                            nextLevel.append(e.left)
                        if e.right:
                            nextLevel.append(e.right)
                    if not currLevel:
                        currLevel, nextLevel = nextLevel, currLevel
                if len(tree_dic) != len(result):
                    isComplete = False
                if isComplete == False:
                    print("not complete")
                else:
                    print(' '.join(result))
        except(EOFError):
            break
