# quickSelect
import random
def select_nth(n,items):
    pivot = random.choice(items)
    lesser = [i for i in items if i < pivot]
    if len(lesser) > n:
        return select_nth(n, lesser)
    n -= len(lesser)

    numequal = items.count(pivot)
    if numequal > n:
        return pivot
    n -= numequal

    greater = [i for i in items if i > pivot]
    return select_nth(n, greater)
items = []
while True:
    try:
        n = int(input())
        items.append(n)
        print(n)
        if len(items) > 1:
            print(select_nth(len(items),items))
    except(EOFError):
        break

