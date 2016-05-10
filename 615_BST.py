'''
Tree

615 Is its a tree?

In this problem you will be given several descriptions of collections of nodes connected by directed edges. For each of these you are to determine if the collection satisfies the definition of a tree or not.

Input
The input will consist of a sequence of descriptions (test cases) followed by a pair of negative integers.  Each test case will consist of a sequence of edge descriptions followed by a pair of zeroes Each edge description will consist of a pair of integers; the first integer identifies the node from which the edge begins, and the second integer identifies the node to which the edge is directed. Node numbers will always be greater than zero.

Output
For each test case display the line ‘Case k is a tree.’ or the line ‘Case k is not a tree.’, where k corresponds to the test case number (they are sequentially numbered starting with 1).
'''
case = 0
tree = {}
root = set()

def travel(s, e, tree, traveled):
    try:
        traveled[tree[e]] = tree[s]
    except(KeyError):
        break
    if e in tree:
        travel(e, tree[e], traveled)

def traveled(root, tree):
    traveled = {}
    print(root, tree)
    for k, v in tree.items():
        if v == root:
            travel(root, k, tree, traveled)
    print(traveled)
    return True


isTree = True
if __name__ == '__main__':
    while True:
        try:
            t = list(map(int, input().split()))
            for i in range(0, len(t), 2):
                if t[i] < 0 and t[i + 1] < 0:
                    break
                elif t[i] == 0 and t[i + 1] == 0:
                    for k, v in tree.items():
                        if k in root:
                            root.remove(k)
                    case += 1

                    if len(root) == 1:
                        for e in root:
                            root_e = e
                    else:
                        isTree = False

                    isTree = traveled(root_e, tree)

                    if len(tree) == len(root) == 0:
                        print("Case ", case, " is a tree.", sep = "")
                    elif isTree == True:
                        print("Case ", case, " is a tree.", sep = "")
                    else:
                        print("Case ", case, " is not a tree.", sep = "")
                    tree = {}
                    root = set()
                    isTree = True
                else:
                    if t[i] != t[i + 1] and t[i + 1] not in tree:
                        tree[t[i + 1]] = t[i]
                        root.add(t[i])
                    else:
                        isTree = False
        except(EOFError):
            break
