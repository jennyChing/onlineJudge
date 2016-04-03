sen = []
max_len = 0
while True:
    try:
        n = input()
        if max_len < len(n):
            max_len = len(n)
        sen.append(n)
    except(EOFError):
        break
sen = sen[::-1]
print(sen)

for i in range(len(sen)):
    for j in range(max_len):
        try:
            print(sen[i][j])
        except(IndexError):
            print(" ")
            continue
0,0 1,0
0,1 1,1
0,2 1,2

