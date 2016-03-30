count = 0
memo = {1:1, 5:2, 10:3, 25:13, 50:50}
def recMC(coinValueList, change):
    print("cc", count)
    if change in memo:
        print(count, memo, memo[change])
        count = memo[change]
    else:
        memo[change] = count
        for i in [c for c in coinValueList if c <= change]:
            print(change-i)
            recMC(coinValueList, change - i)

print(recMC([1,5,10,25],11))
