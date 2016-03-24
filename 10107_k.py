def kth(lst,k):
    p = lst[0]
    L = []
    R = []
    for i in range(1,len(lst)):
        if p > lst[i]:
            L.append(lst[i])
        else:
            R.append(lst[i])
    if len(L) == k-1:
        return p
    if len(L) >= k:
        return kth(L,k)
    return kth(R,k-len(L)-1)

lst = []

while True:
    try:
        n = int(input())
        lst.append(n)
# if len(lst) is odd: do kth twice
        if len(lst)%2:
            print(kth(lst, len(lst) // 2 + 1))
        else:
            print(((kth(lst, len(lst) // 2)) + kth(lst, len(lst) // 2 + 1)) // 2)
    except(EOFError):
        break

