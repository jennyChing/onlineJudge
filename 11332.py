def sum_digits(n,sum_d):
    for i in range(0,len(n)):
        sum_d = sum_d + int(n[i])
    if sum_d < 10:
        return sum_d
    if sum_d >= 10:
       return sum_digits(str(sum_d),0)
if __name__ == "__main__":
    while True:
        try:
            n = input()
            if n == "0":
                break
            g = sum_digits(n,0)
            print(g)
        except(EOFError):
            break

