'''
Primes

524 - Prime Ring Problem

A ring is composed of n (even number) circles as shown in diagram.  Put natural numbers 1, 2, . . . , n into each circle separately, and the sum of numbers in two adjacent circles should be a prime. Note: the number of first circle should always be 1.

Input
n (0 < n ≤ 16)

Output
The output format is shown as sample below. Each row represents a series of circle numbers in the ring beginning from 1 clockwisely and anticlockwisely. The order of numbers must satisfy the above requirements. You are to write a program that completes above process.
'''
#def prime():
#    isPrime = [True for _ in range(32)] # 2 * i + 1= n
#    isPrime[0], isPrime[1] = False, False
#    buff = set()
#    for i in range(len(isPrime)):
#        if isPrime[i]:
#            buff.add(i)
#            for j in range(i * i, len(isPrime), i):
#                isPrime[j] = False
#    return buff

'''
Append primes to a dict after using them as the prime eliminator
'''
def solve(par):
    def fill(step):
        if step == N - 1:
            for i in range(2, N + 1):
                if i not in ring and i + 1 in Primes:
                    ring.append(i)
                    results.append(tuple(ring))
                    ring.pop()
            return
        for i in range(2, N + 1):
            if i not in ring and i + ring[-1] in Primes:
                ring.append(i)
                fill(step + 1)
                ring.pop()
    N = par
    ring = [1]
    results = []
    fill(1)
    for i in range(len(results)):
        results[i] = ' '.join(str(e) for e in results[i])
    return results

if __name__ == '__main__':
    Primes = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])
    cases = 0
    memo = {}
    while True:
        try:
            n = int(input())
        except(EOFError):
            break
        cases += 1
        if cases > 1:
            print(memo)
        if n in memo:
            results = memo[n]
        else:
            results = solve(n)
            memo[n] = results
        print("Case ", cases, ':', sep="")
        for r in results:
            print(r)
