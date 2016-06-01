import math
'''
Prime

10140 - Prime Distance

Your program is given 2 numbers: L and U (1 ≤ L < U ≤ 2, 147, 483, 647), and you are to find the two adjacent primes C1 and C2 (L ≤ C1 < C2 ≤ U) that are closest (i.e. C2 − C1 is the minimum). If there are other pairs that are the same distance apart, use the first pair. You are also to find the two adjacent primes D1 and D2 (L ≤ D1 < D2 ≤ U) where D1 and D2 are as distant from each other as possible (again choosing the first pair if there is a tie).
'''

# only go through prime numbers smaller then n^1/2:
# go through prime numbers under 1000000^1/2 to bulid a list, and cross out multiples of prime numbers one by one. Those not crossed out are prime numbers

# primes within (1000000^1/2)
def prime():
    isPrime = [True for _ in range(21474830)] # 2 * i + 1= n
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
            lst = []
            l, r = list(map(int, input().split()))
            for a in sortedPrimes:
                if a >= l and a <= r:
                    lst.append(a)
            if len(lst) > 1:
                close, far = [], []
                min_d, max_d = float('inf'), 0
                for i in range(len(lst) - 1):
                    d = lst[i + 1] - lst[i]
                    if d < min_d:
                        min_d = d
                        close = lst[i:i + 2]
                    if d > max_d:
                        max_d = d
                        far = lst[i:i + 2]
                print(close[0], ',', close[1], " are closest, ", far[0], ',', far[1], " are most distant.", sep="")
            else:
                print("There are no adjacent primes.")
        except(EOFError):
            break



