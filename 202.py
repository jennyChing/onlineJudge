'''
Cycle Finding:  Memoization

202 - Repeating Decimals

Write a program that reads numerators and denominators of fractions and determines their repeating cycles.  For the purposes of this problem, define a repeating cycle of a fraction to be the first minimal length string of digits to the right of the decimal that repeats indefinitely with no intervening digits. Thus for example, the repeating cycle of the fraction 1/250 is 0, which begins at position 4 (as opposed to 0 which begins at positions 1 or 2 and as opposed to 00 which begins at positions 1 or 4).
'''
from decimal import *
import math
getcontext().prec = 1000

def fractionToDecimal(n, d):
    sign = '-' if n * d < 0 else ''
    head, remainder = divmod(abs(n), abs(d))
    tail, see = '', {}
    while remainder != 0:
        if remainder in seen:
            tail = tail[: seen[remainder]]

if __name__ =='__main__':
    while True:
        try:
            n1, n2 = list(map(int, input().split()))
        except(EOFError):
            break

        t = Decimal(n1) / Decimal(n2)
        print(t)

