int_sum = 0
while True:
    try:
        value = int(input())
        #value = value[::-1]
        if value == "0":
            break
        int_sum = int_sum + value
        #result = str(int_sum)[::-1]
    except(EOFError):
        break
print(int_sum)
