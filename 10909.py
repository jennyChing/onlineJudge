'''
BST with ranking

10909 - Lucky Number

Lucky numbers are defined by a variation of the well-known sieve of Eratosthenes. Beginning with the natural numbers strike out all even ones, leaving the odd numbers 1, 3, 5, 7, 9, 11, 13, . . .  The second number is 3, next strike out every third number, leaving 1, 3, 7, 9, 13, . . . The third number is 7, next strike out every seventh number and continue this process infinite number of times. The numbers surviving are called lucky numbers. The first few lucky numbers are:
    1, 3, 7, 9, 13, 15, 21, 25, 31, 33, . . . . . .
    In this problem your task is to test whether a number can be written as the sum of two lucky numbers.
'''
def cal_lucky():
    lucky = []
    for i in range(1, 2000000, 2):
        lucky.append(i)
    for j in range(1, len(lucky)):
        try:
            lucky = [v for i, v in enumerate(lucky) if (i + 1) % lucky[j] != 0]
        except(IndexError):
            break
    print(lucky)
    lucky_set = set()
    for e in lucky:
        lucky_set.add(e)
    return lucky_set

if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            lucky = cal_lucky()
            isLucky = False
            a, b = 0, 0
            for i in range(1, n // 2):
                if i in lucky and n - i in lucky:
                    isLucky = True
                    a, b = i, n - i
                    break
            if isLucky == False:
                print(n, "is not the sum of two luckies!")
            else:
                print(n, " is the sum of ", a, " and ", b, ".", sep = "")

        except(EOFError):
            break
