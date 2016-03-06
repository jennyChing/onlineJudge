def row_new(lst,max_n,n,k):
    if n >= k:
        max_n = max_n + int(n/k)
        row_new(lst,max_n,n%k+int(n/k),k)
        lst.append(max_n)
if __name__ == "__main__":
    while True:
        try:
            value = list(map(int, input().split()))
            n = value[0]
            k = value[1]
            max_n = n
            lst = []
            row_new(lst,max_n,n,k)
            print(lst[0])
        except(EOFError):
            break
