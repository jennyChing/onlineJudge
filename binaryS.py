def biSearch (a, n):
    left = 0
    right = len(a)
    while right > left:
        middle = int((right+left)/2)
        print(left,right,middle,a[middle],n)
        if n == a[middle]:
            return middle
            print(middle)
        elif n > a[middle]:
            left = middle+1
        else:
            right = middle
    return None
while True:
    try:
        a = list(map(int,input().split()))
        n = int(input())
        print(biSearch(a, n))
    except(EOFError):
        break
