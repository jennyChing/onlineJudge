sky = [0 for _ in range(10000)]
if __name__ == '__main__':
    while True:
        try:
            rec = list(map(int,input().split()))
            l, h, r = rec[0], rec[1], rec[2]
            for i in range(l, r):
                sky[i] = max(sky[i], h)
        except(EOFError):
            break

for i in range(len(sky) - 1):
    if sky[i] != sky[i + 1]:
        print(i + 1, sky[i + 1], end = " ")
print()

