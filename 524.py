'''
Primes

524 - Prime Ring Problem

A ring is composed of n (even number) circles as shown in diagram.  Put natural numbers 1, 2, . . . , n into each circle separately, and the sum of numbers in two adjacent circles should be a prime. Note: the number of first circle should always be 1.

Input
n (0 < n ≤ 16)

Output
The output format is shown as sample below. Each row represents a series of circle numbers in the ring beginning from 1 clockwisely and anticlockwisely. The order of numbers must satisfy the above requirements. You are to write a program that completes above process.
'''
def prime():
    isPrime = [True for _ in range(1000)] # 2 * i + 1= n
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
