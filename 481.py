'''
Longest increase seq

481 - What Goes Up

Write a program that will select the longest strictly increasing subsequence from a sequence of integers.
'''
def read():
    value = []
    while True:
        try:
            v = int(input())
            value.append([v])
        except(EOFError):
            return value

if __name__ == '__main__':
    value = read()
    for i in range(len(value)):
        temp = value[i][0]
        for j in range(i + 1, len(value)):
            if value[j][0] > temp:
                temp = value[j][0]
                value[i].append(value[j][0])
    print(value)
    for i in range(len(value)):
        for j in range(i, 0, -1):
            if value[j][0] < value[i][0]:
                value[i].insert(0, value[j][0])
    print(value)
    max_len = sorted(max(value, key = len))
    print(len(max_len))
    print('-')
    for l in max_len:
        print(l)
