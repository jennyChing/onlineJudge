'''
Primes

10311 - Goldbach and Euler

Input
The input file contains 100000 lines of input. Each line contains a single integer n (0 < n ≤ 100000000).

Output
For each line of input produce one line of output. This line should be of one of the following types:
    n is not the sum of two primes!
    n is the sum of p1 and p2.
For the second case, always make sure that (p2 − p1) is positive and minimized.
'''
def prime():
    isPrime = [True for _ in range(1000001)] # 2 * i + 1= n
    isPrime[0], isPrime[1] = False, False
    buff = set()
    for i in range(len(isPrime)):
        if isPrime[i]:
            buff.add(i)
            for j in range(i * i, len(isPrime), i):
                isPrime[j] = False
    return buff

if __name__ =='__main__':
    primes = prime()
    sortedPrimes = sorted(primes)
    while True:
        try:
            n = int(input())
        except(EOFError):
            break
        for a in sortedPrimes:
            if n - a in primes:
                print(n, " is the sum of ", a, " and ", n - a, ".", sep='')
                break
        else:
            print(n, "is not the sum of two primes!")

