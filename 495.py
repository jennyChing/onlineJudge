def fib(n):
    while n - 1 not in memo:
        fib(n - 1)
    else:
        memo[n] = memo[n - 1] + memo[n - 2]
        print(memo)
        return memo[n]

if __name__ == "__main__":
    while True:
        try:
            memo= {0:0, 1:1, 2:1}
            n = int(input())
            print("The Fibonacci number for", n, "is", fib(n))
        except(EOFError):
            break
