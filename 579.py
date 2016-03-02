while True:
    try:
        time = list(map(int,input().split(":")))
        x = time[0]
        y = time[1]
        if x == 0 and y == 0:
            break
        if 6*y > 30*x+0.5*y:
            angle = 5.5*y-30*x
        else:
            angle = -5.5*y+30*x
        if angle >= 180:
            angle = 360 - angle
        print("{0:.3f}".format(round(angle,3)))
    except(EOFError):
        break


