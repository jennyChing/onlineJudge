'''
Binary search tree

10303 - How Many Trees?
Given a number n, can you tell how many different binary search trees may be constructed with a set of numbers of size n such that each element of the set will be associated to the label of exactly one node in a binary search tree?

Solution:
    Dynamic programming in recursive function to calculate the numbers of left and right sub-trees
'''
def cal_tree(n, bst):
    if n not in bst:
        temp = 0
        for i in range(n):
            temp += cal_tree(i, bst) * cal_tree(n - i - 1, bst)
        bst[n] = temp
        return bst[n]
    else:
        return bst[n]

if __name__ == '__main__':
    while True:
        try:
            n = int(input())
        except(EOFError):
            break
        bst = {0:1, 1:1, 2:2, 3:5}
        print(cal_tree(n, bst))
