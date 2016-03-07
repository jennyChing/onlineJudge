if __name__ == "__main__":
    while True:
        try:
            value = input()
            skew = 0
            if value == "0":
                break
            value = value[::-1]
            for i in range(0,len(value)):
                skew = int(value[i])*(2**(i+1)-1) + skew
            print(skew)
        except(EOFError):
            break
