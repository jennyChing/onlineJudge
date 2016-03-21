def atoi(string):
    total = 0
    for ch in string:
# turn character into int by using ASCII code minus '0's ASCII code
        total = total*10 + ord(ch)-ord('0')
    return total
while True:
    try:
        string = input()
        sign = -1 if string[0] == "-" else 1
# use tenary
        total = atoi(string[1:] if string[0] == "-" else string)
        assert sign*total == int(string), "wrong output"
        print(total*sign)
    except(EOFError):
        break

