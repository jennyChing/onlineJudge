# read and split the input
# read the first number as v and the second as t and print the resulti
while True:
    try:
        value = list(map(int, input().split()))
        result = value[0] * value[1] * 2
        print(result)
    except (EOFError):
        break
