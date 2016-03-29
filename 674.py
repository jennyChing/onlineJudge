'''
674 - Coin Change:
Suppose there are 5 types of coins: 50-cent, 25-cent, 10-cent, 5-cent, and 1-cent. We want to make changes with these coins for a given amount of money.  For example, if we have 11 cents, then we can make changes with one 10-cent coin and one 1-cent coin, two 5-cent coins and one 1-cent coin, one 5-cent coin and six 1-cent coins, or eleven 1-cent coins.  So there are four ways of making changes for 11 cents with the above coins. Note that we count that there is one way of making change for zero cent.  Write a program to find the total number of different ways of making changes for any amount of money in cents. Your program should be able to handle up to 7489 cents.
'''
while True:
    try:
        n = int(input())
        memo = {}
        a = n // 5
        b = n // 10
        c = n // 25
        d = n // 50
        changes = 0
        for i in range(d+1):
            for j in range(c+1):
                for k in range(b+1):
                    for h in range(a+1):
                        if i * 50 + j * 25 + k * 10 + h * 5 < n:
                            print(h, k, j, i)
                            changes += 1
        print(changes)
    except(EOFError):
        break
