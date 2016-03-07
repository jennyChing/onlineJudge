import math
def factors_sum(n):
    f_lst = set()
    for i in range(1,math.ceil(n**(.5))+1):
        if n%i == 0:
            f_lst.add(i)
            f_lst.add(int(n/i))
    f_lst.discard(n)
    return sum(f_lst)
print("PERFECTION OUTPUT")
while True:
    try:
        p = [6, 28, 496, 8128]
        value = list(map(int, input().split()))
        for i in range(0,len(value)):
            f_sum = factors_sum(value[i])
            if value[i] == 0:
                print("END OF OUTPUT")
                break
            elif value[i] in p:
                print('{0:5d}'.format(value[i])," PERFECT")
            elif f_sum < value[i]:
                print('{0:5d}'.format(value[i]), " DEFICIENT")
            elif f_sum > value[i]:
                print('{0:5d}'.format(value[i])," ABUNDANT")
    except(EOFError):
        break
