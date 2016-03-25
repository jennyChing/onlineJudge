'''
10110 Light, more light:
There is man named ”mabu” for switching on-off light in our University. He switches on-off the lights in a corridor. Every bulb has its own toggle switch. That is, if it is pressed then the bulb turns on.  Another press will turn it off. To save power consumption (or may be he is mad or something else) he does a peculiar thing. If in a corridor there is n bulbs, he walks along the corridor back and forth n times and in i-th walk he toggles only the switches whose serial is divisable by i. He does not press any switch when coming back to his initial position. A i-th walk is defined as going down the corridor (while doing the peculiar thing) and coming back again. Now you have to determine what is the final condition of the last bulb. Is it on or off?
'''
while True:
    try:
        n = int(input())
        if n == 0:
            break
        print("yes" if n**(.5) %1 ==0 else "no")
    except(EOFError):
        break
