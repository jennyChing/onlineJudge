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
p_sen = []
for j in range(max_len):
    for i in range(len(sen)):
        try:
            print(sen[i][j], end = "")
            if i == len(sen) - 1:
                print()
        except(IndexError):
            print(" ")
            continue
