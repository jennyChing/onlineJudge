def median(lst):
    lst =   sorted(lst)
    if len(lst) < 1:
        return None
    if len(lst) %2 == 1:
        return lst[int(((len(lst)+1)/2)-1)]
    else:
        return int((lst[int((len(lst)/2)-0.5)]+lst[int((len(lst)/2)+0.5)])/2.0)
lst = []
while True:
    try:
        n = int(input())
        lst.append(n)
        print(median(lst))
    except(EOFError):
        break

