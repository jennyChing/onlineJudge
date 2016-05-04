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
        max_LIS = []
        for j in range(i + 1, len(value)):
            if value[j][0] > temp:
                temp = value[j][0]
                value[i].append(value[j][0])
    max_len = 1
    for i in range(len(value)):
        if len(value[i]) > max_len:
            print(value[i])
    print(value)



