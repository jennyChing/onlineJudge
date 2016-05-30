'''
Primes

406 - Prime Cuts

Input

Each input set will be on a line by itself and will consist of 2 numbers. The first number is the maximum number in the complete list of prime numbers between 1 and N. The second number defines the C*2 prime numbers to be printed from the center of the list if the length of the list is even; or the (C*2)-1 numbers to be printed from the center of the list if the length of the list is odd. (the list refers to all the primes smaller then N)

Output

For each input set, you should print the number N beginning in column 1 followed by a space, then by the number C, then by a colon (:), and then by the center numbers from the list of prime numbers as defined above. If the size of the center list exceeds the limits of the list of prime numbers between 1 and N, the list of prime numbers between 1 and N (inclusive) should be printed. Each number from the center of the list should be preceded by exactly one blank. Each line of output
should be followed by a blank line. Hence, your output should follow the exact format shown in the sample output. (start printing from the middle of the list)
'''
import math
def prime():
    isPrime = [True for _ in range(100000)] # 2 * i + 1= n
    isPrime[0], isPrime[1] = False, False
    buff = set()
    for i in range(len(isPrime)):
        if isPrime[i]:
            buff.add(i)
            for j in range(i * i, len(isPrime), i):
                isPrime[j] = False
    buff.add(1)
    return buff
if __name__ == '__main__':
    primes = prime()
    sortedPrimes = sorted(primes)
    while True:
        try:
            n, c = list(map(int, input().split()))
            lst = []
            for p in sortedPrimes:
                if p <= n:
                    lst.append(p)
            m = len(lst)//2
            r = len(lst)%2
            if c >= len(lst):
                print(n, ' ',  c, ':', sep="", end="")
                for i in range(len(lst)):
                    if i == m - c and i > 0:
                        print(lst[i], end="")
                    elif i >= 0:
                        print("", lst[i], end="")
                print()
            elif r == 0:
                print(n, ' ',  c, ':', sep="", end="")
                for i in range(m - c, m + c):
                    if i == m - c and i > 0:
                        print(lst[i], end="")
                    elif i >= 0:
                        print("", lst[i], end="")
                print()
            else:
                print(n, ' ',  c, ':', sep="", end="")
                for i in range(m - c + 1, m + c):
                    if i == m - c + 1 and i > 0:
                        print(lst[i], end="")
                    elif i >= 0:
                        print("", lst[i], end="")
                print()
            print()
        except(EOFError):
            break
