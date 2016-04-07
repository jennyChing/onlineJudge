import sys

def init(n):
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]

def fib(n):
    if n not in memo:
        memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]

if __name__ == "__main__":
    #sys.setrecursionlimit(5000)
    memo= {0:0, 1:1}
    init(5000)
    while True:
        try:
            n = int(input())
            print("The Fibonacci number for", n, "is", fib(n))
            #print("The Fibonacci number for", n, "is", memo[n])
        except(EOFError):
            break
