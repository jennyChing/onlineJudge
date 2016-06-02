'''
Primes

11408 - Count DePrimes

Input
Each line contains a and b in the format ‘a b’. 2 ≤ a ≤ 5000000. a ≤ b ≤ 5000000.  Input is terminated by a line containing ‘0’.

Output
Each line should contain the number of DePrimes for the corresponding test case.  Explanation: In Test Case 2, take 10. Its Prime Factors are 2 and 5. Sum of Prime Factors is 7, which is a prime.  So, 10 is a DePrime.

1. a < i < b; 2. i = prime * prime; 3. prime + prime = prime
'''
import math
# only go through prime numbers smaller then n^1/2:
# go through prime numbers under 1000000^1/2 to bulid a list, and cross out multiples of prime numbers one by one. Those not crossed out are prime numbers
# primes within (1000000^1/2)

def prime():
    isPrime = [True for _ in range(5000000)] # 2 * i + 1= n
    isPrime[0], isPrime[1] = False, False
    buff = set()
    for i in range(len(isPrime)):
        if isPrime[i]:
            buff.add(i)
            for j in range(i * i, len(isPrime), i):
                isPrime[j] = False
    return buff

if __name__ == '__main__':
    primes = prime()
    sortedPrimes = sorted(primes)
    while True:
        try:
            n = input()
            if n == '0':
                break
            a, b = list(map(int, n.split()))
            dePrimes = []
            for i in range(a, b + 1):
                factors = []
                for p1 in sortedPrimes:
                    if p1 < b + 1:
                        p2 = i / p1
                        if p2 % 1 == 0:
                            factors.append(p1)
                if sum(factors)in primes:
                    dePrimes.append(i)
            print(len(dePrimes))
        except(EOFError):
            break
