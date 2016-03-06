def median(lst):
    lst =   sorted(lst)
    if len(lst) < 1:
        return None
    if len(lst) %2 == 1:
        return lst[int(((len(lst)+1)/2)-1)]
    else:
        return int((lst[int((len(lst)/2)-0.5)]+lst[int((len(lst)/2)+0.5)])/2.0)
while True:
    try:
        cases = int(input())
        for i in range(0,cases):
            houses = list(map(int, input().split()))
            #relatives = houses[0]
            m = median(houses[1:])
            distance = 0
            for j in range(1, len(houses)):
                distance = distance + abs(m-houses[j])
            print(distance)
    except(EOFError):
        break
