'''
Dynamic Programming***
573 - The Snail:
A snail is at the bottom of a 6-foot well and wants to climb to the top. The snail can climb 3 feet while the sun is up, but slides down 1 foot at night while sleeping. The snail has a fatigue factor of 10%, which means that on each successive day the snail climbs 10% times$ 3 = 0.3 feet less than it did the previous day. (The distance lost to fatigue is always 10% of the first day's climbing distance.) On what day does the snail leave the well, i.e., what is the first day during which the snail's height exceeds 6 feet? (A day consists of a period of sunlight followed by a period of darkness.) As you can see from the following table, the snail leaves the well during the third day.
'''
if __name__ == '__main__':
    while True:
        try:
            value = list(map(int, input().split()))
            day = 1
            H, U, D, F = value[0], value[1], value[2], value[3]
            h = U - D
            isFail = False
            if H == 0:
                break
            if U - D > H:
                break
            while h < H:
                day += 1
                h = h + U * (1 - (F * 0.01 * (day - 1)))
                print(day, "climb:", U * (day - 1) * (1 - (F * 0.01)), "slide:", D, "height:", h)
                if h >= H:
                    break
                h -= D
                if h <= 0:
                    isFail = True
                    break
            if isFail == True:
                print("failure on day", day)
            else:
                print("success on day", day)

        except(EOFError):
            break
