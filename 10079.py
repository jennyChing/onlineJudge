while True:
    try:
        cuts = int(input())
        if cuts < 0:
            break
        elif cuts ==0:
            pizza = 1
        else:
            pizza = (cuts*(cuts + 1) + 2)>>1
        print(pizza)
    except(EOFError):
        break
