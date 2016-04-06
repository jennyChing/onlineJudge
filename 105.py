import math
lst = []
l_min = math.inf
r_max = 0
if __name__ == '__main__':
    while True:
        try:
            rec = list(map(int,input().split()))
            lst.append(rec)
        except(EOFError):
            break

for l, h, r in lst:
    l_min = min(l_min, l)
    r_max = max(r_max, r)

sky = [0 for _ in range(r_max - l_min + 1)]
for l, h, r in lst:
    for i in range(l - l_min, r - l_min):
        sky[i] = max(sky[i], h)
print(l_min, sky[0], end = " ")
for i in range(len(sky) - 1):
    if sky[i] != sky[i + 1]:
        print(i + 1 + l_min, sky[i + 1], end = " ")
print()
