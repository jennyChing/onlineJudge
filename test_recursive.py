def rec(n ,memo):
    if n in memo:
        return memo[n]
    else:
        temp = 0
        for i in range(n):
            temp += 1
        memo[n] = temp
        print(memo)
    return memo[n]
if __name__ == '__main__':
    memo = {}
    print(rec(2, memo))
