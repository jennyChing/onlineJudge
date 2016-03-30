import math
# only go through prime numbers smaller then n^1/2:
# go through prime numbers under 1000000^1/2 to bulid a list, and cross out multiples of prime numbers one by one. Those not crossed out are prime numbers

# primes within (1000000^1/2)
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

#def prime(n, memo):
#    if n in memo:
#        return True
#    if n % 2 == 0:
#        return False
#    if n > 2:
#        for i in range(3, math.ceil(n**(.5)) + 1, 2):
#            if n % i == 0:
#                return False
#        memo.append(n)
#    return True
if __name__ == '__main__':
    primes = prime()
    sortedPrimes = sorted(primes)
    while True:
        try:
            n = int(input())
            if n == 0:
                break
            for a in sortedPrimes:
                if n - a in primes:
                    print(n, "=", a, "+", n - a)
                    break
            else:
                print("Goldbach's conjecture is wrong.")
        except(EOFError):
            break



