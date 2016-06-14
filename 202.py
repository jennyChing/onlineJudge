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
    tail, seen = '', {}
    isCycle = False
    while remainder != 0:
        if remainder in seen:
            tail = tail[: seen[remainder]] + '(' + tail[seen[remainder]:] + ')'
            isCycle = True
            break
        seen[remainder] = len(tail)
        digit, remainder = divmod(remainder * 10, abs(d))
        tail += str(digit)
    return sign + str(head) + tail and '.' + tail, isCycle, seen, remainder

cnt = 0

if __name__ =='__main__':
    while True:
        try:
            n, d = list(map(int, input().split()))
        except(EOFError):
            break
        frac, isCycle, seen, remainder = fractionToDecimal(n, d)
        #if cnt > 0:
        print()
        if isCycle == False:
            print(n, '/', d, ' = ', n//d, frac, '(0)', sep="")
            print("   1 = number of digits in repeating cycle")
        elif len(frac) > 50:
            print(n, '/', d, ' = ', n//d, frac[:52], '...)', sep="")
            print("  ", len(frac) - 3 - seen[remainder], "= number of digits in repeating cycle")
        else:
            print(n, '/', d, ' = ', n//d, frac, sep="")
            print("  ", len(frac) - 3 - seen[remainder], "= number of digits in repeating cycle")
        cnt += 1
