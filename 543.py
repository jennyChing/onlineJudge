import math
# only go through prime numbers smaller then n^1/2:
def prime(n, memo):
    if n in memo:
        return True
    if n % 2 == 0:
        return False
    if n > 1:
        for i in range(3, math.ceil(n**(.5)) + 1, 2):
            if n % i == 0:
                return False
        memo.append(n)
    return True
if __name__ == '__main__':
    memo = [2]
    while True:
        n = int(input())
        if n == 0:
            break
        if prime(n - 2, memo):
            print(n, "=", 2, "+", n - 2)
        else:
            for i in range(3, n, 2):
                if prime(i, memo) == True and prime(n - i, memo) == True:
                    print(n, "=", i, "+", n - i)
                    break

