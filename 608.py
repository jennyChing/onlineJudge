'''
set search - array
608 - Counterfeit Dollar

Sally Jones has a dozen Voyageur silver dollars. However, only eleven of the coins are true silver dollars; one coin is counterfeit even though its color and size make it indistinguishable from the real silver dollars. The counterfeit coin has a different weight from the other coins but Sally does not know if it is heavier or lighter than the real coins.

Input
The first line of input is an integer n (n > 0) specifying the number of cases to follow. Each case consists of three lines of input, one for each weighing. Sally has identified each of the coins with the letters A–L. Information on a weighing will be given by two strings of letters and then one of the words “up”, “down”, or “even”. The first string of letters will represent the coins on the left balance; the second string, the coins on the right balance. (Sally will always place the same number of coins on the right balance as on the left balance.) The word in the third position will tell whether the right side of the balance goes up, down, or remains even.

Output
For each case, the output will identify the counterfeit coin by its letter and tell whether it is heavy or light. The solution will always be uniquely determined.

Solution:
    Solve different cases based on how many up/downs are appeared in the 3 weighting results:
    case1: all evens - see which coin are not in the set called 'real'
    case2: one up or down - examine each coin appeared in this result and exclude the coins in the set named 'real'
    case3: two up or down - examine each coin appeared twice in un-even results and exclude the coins in the set named 'real'
    case4: three up or down - examine each coin appeared three times in the dictionary called feit and exclude the coins in the set named 'real'

New Tips - set:
    >>> a = set('abracadabra')
    >>> b = set('alacazam')
    >>> a                                  # unique letters in a
    {'a', 'r', 'b', 'c', 'd'}
    >>> a - b                              # letters in a but not in b
    {'r', 'd', 'b'}
    >>> a | b                              # letters in either a or b
    {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
    >>> a & b                              # letters in both a and b
    {'a', 'c'}
    >>> a ^ b                              # letters in a or b but not both
    {'r', 'd', 'b', 'm', 'z', 'l'}
'''
def read ():
    coins = []
    cnt = 0
    for n in range(3):
        c = list(map(str, input().split()))
        if c[2] != 'even':
            cnt += 1
        coins.append(c)
    return coins, cnt

def process_up(i):
# left is heavy and right is light
    for left in str(coins[i][0]):
        if left in real:
            pass
        elif left in light:
            real.add(str(left))
            pass
        elif left in heavy:
            feit[left] += 1
            pass
        else:
            feit[left] = 1
            heavy.add(str(left))
        #print(real, heavy, light)
    for right in str(coins[i][1]):
        if right in real:
            pass
        elif right in heavy:
            real.add(str(right))
            pass
        elif right in light:
            feit[right] += 1
            pass
        else:
            feit[right] = 1
            light.add(str(right))
        #print(real, heavy, light)

def process_down(i):
# right is heavy and left is light
    for left in str(coins[i][0]):
        if left in real:
            pass
        elif left in heavy:
            real.add(str(left))
            pass
        elif left in light:
            feit[left] += 1
            pass
        else:
            light.add(str(left))
            feit[left] = 1
        #print(real, heavy, light)
    for right in str(coins[i][1]):
        if right in real:
            pass
        elif right in light:
            real.add(str(right))
            pass
        elif right in heavy:
            feit[right] += 1
            pass
        else:
            feit[right] = 1
            heavy.add(str(right))

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        heavy = set()
        light = set()
        real = set()
# store the cnts of how many time each coin appears in up or down
        feit = {}
        coins, case = read()
        all_c = {'A','B','C','D','E','F','G','H','I','J','K','L'}
# Case 1: all even
        if case == 0:
            for i in range(3):
                for left in coins[i][0]:
                    real.add(left)
                for right in coins[i][1]:
                    real.add(right)
            k = all_c - real
            for ac in k:
                print(ac, "is the counterfeit coin and it is heavy.")
# Cases 2: one up/down
        elif case == 1:
            for i in range(3):
                if coins[i][2] == 'up':
                    process_up(i)
                elif coins[i][2] == 'down':
                    process_down(i)
                elif coins[i][2] == 'even':
                    for left in coins[i][0]:
                        real.add(left)
                    for right in coins[i][1]:
                        real.add(right)
            for f, value in feit.items():
                if f in heavy and f not in real:
                    print(f, "is the counterfeit coin and it is heavy.")
                if f in light and f not in real:
                    print(f, "is the counterfeit coin and it is light.")
# Cases 3: two up/downs
        elif case == 2:
            for i in range(3):
                if coins[i][2] == 'up':
                    process_up(i)
                elif coins[i][2] == 'down':
                    process_down(i)
                elif coins[i][2] == 'even':
                    for left in coins[i][0]:
                        real.add(left)
                    for right in coins[i][1]:
                        real.add(right)
            for f, value in feit.items():
                if value == 2:
                    if f in heavy and f not in real:
                        print(f, "is the counterfeit coin and it is heavy.")
                    if f in light and f not in real:
                        print(f, "is the counterfeit coin and it is light.")
# Cases 4: two up/downs
        elif case == 3:
            for i in range(3):
                if coins[i][2] == 'up':
                    process_up(i)
                elif coins[i][2] == 'down':
                    process_down(i)
                elif coins[i][2] == 'even':
                    for left in coins[i][0]:
                        real.add(left)
                    for right in coins[i][1]:
                        real.add(right)
            for f, value in feit.items():
                if value == 3:
                    if f in heavy and f not in real:
                        print(f, "is the counterfeit coin and it is heavy.")
                    if f in light and f not in real:
                        print(f, "is the counterfeit coin and it is light.")
