'''
set search - array
608 - Counterfeit Dollar

Sally Jones has a dozen Voyageur silver dollars. However, only eleven of the coins are true silver dollars; one coin is counterfeit even though its color and size make it indistinguishable from the real silver dollars. The counterfeit coin has a different weight from the other coins but Sally does not know if it is heavier or lighter than the real coins.

Input
The first line of input is an integer n (n > 0) specifying the number of cases to follow. Each case consists of three lines of input, one for each weighing. Sally has identified each of the coins with the letters A–L. Information on a weighing will be given by two strings of letters and then one of the words “up”, “down”, or “even”. The first string of letters will represent the coins on the left balance; the second string, the coins on the right balance. (Sally will always place the same number of coins on the right balance as on the left balance.) The word in the third position will tell whether the right side of the balance goes up, down, or remains even.

Output
For each case, the output will identify the counterfeit coin by its letter and tell whether it is heavy or light. The solution will always be uniquely determined.

Solution:
    find the balance of coins that are not even, and go through the coins to find the one not appeared in the rest comparison which are even
'''
def read ():
    coins = []
    for n in range(3):
        c = list(map(str, input().split()))
        coins.append(c)
    return coins

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        heavy = set()
        light = set()
        real = set()
        feit = set()
        coins = read()
        for i in range(3):
            if coins[i][2] == 'even':
                for left in str(coins[i][0]):
                    real.add(str(left))
                for right in str(coins[i][1]):
                    real.add(str(right))
            elif coins[i][2] == 'up':
# left is heavy and right is light
                for left in str(coins[i][0]):
                    if left in real:
                        pass
                    elif left in light:
                        real.add(str(left))
                        pass
                    elif left in heavy:
                        feit.add(str(left))
                        pass
                    else:
                        heavy.add(str(left))
                    #print(real, heavy, light)
                for right in str(coins[i][1]):
                    if right in real:
                        pass
                    elif right in heavy:
                        real.add(str(right))
                        pass
                    elif right in light:
                        feit.add(str(right))
                        pass
                    else:
                        light.add(str(right))
                    #print(real, heavy, light)
            elif coins[i][2] == 'down':
# right is heavy and left is light
                for left in str(coins[i][0]):
                    if left in real:
                        pass
                    elif left in heavy:
                        real.add(str(left))
                        pass
                    elif left in light:
                        feit.add(str(left))
                        pass
                    else:
                        light.add(str(left))
                    #print(real, heavy, light)
                for right in str(coins[i][1]):
                    if right in real:
                        pass
                    elif right in light:
                        real.add(str(right))
                        pass
                    elif right in heavy:
                        feit.add(str(right))
                        pass
                    else:
                        heavy.add(str(right))
                    #print(right, "add", real, heavy, light)
        heavy.difference_update(real)
        feit.difference_update(real)
        light.difference_update(real)
        print(feit, real, heavy, light)
        all_c = {'A','B','C','D','E','F','G','H','I','J','K','L'}
        if not feit and not heavy and not light:
            for ac in all_c:
                if ac not in real:
                    print(ac, "is the counterfeit coin and it is heavy.")
        if len(feit) == 1:
            for f in feit:
                if f in heavy:
                    print(f, "is the counterfeit coin and it is heavy.")
                if f in light:
                    print(f, "is the counterfeit coin and it is light.")
        else:
            if len(heavy) == 1:
                for h in heavy:
                    print(h, "is the counterfeit coin and it is heavy.")
            if len(light) == 1:
                for l in light:
                    print(l, "is the counterfeit coin and it is light.")




