'''
Binary search tree

10303 - How Many Trees?
Given a number n, can you tell how many different binary search trees may be constructed with a set of numbers of size n such that each element of the set will be associated to the label of exactly one node in a binary search tree?
'''
def cal_tree(n):
    if n not in bst:
        bst[n] = 0
        for i in range(n):
            bst[n] += cal_tree(i) * cal_tree(n - i - 1)
            print("n", cal_tree(i), cal_tree(n - i - 1), bst[n])
    else:
        return bst[n]

if __name__ == '__main__':
    while True:
        try:
            n = int(input())
        except(EOFError):
            break
        bst = {0:1, 1:1, 2:2, 3:5}
        print(bst)
        print(cal_tree(n))
