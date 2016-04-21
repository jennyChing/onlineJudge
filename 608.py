'''
set search - array
608 - Counterfeit Dollar

Sally Jones has a dozen Voyageur silver dollars. However, only eleven of the coins are true silver dollars; one coin is counterfeit even though its color and size make it indistinguishable from the real silver dollars. The counterfeit coin has a different weight from the other coins but Sally does not know if it is heavier or lighter than the real coins.

Input
The first line of input is an integer n (n > 0) specifying the number of cases to follow. Each case consists of three lines of input, one for each weighing. Sally has identified each of the coins with the letters A–L. Information on a weighing will be given by two strings of letters and then one of the words “up”, “down”, or “even”. The first string of letters will represent the coins on the left balance; the second string, the coins on the right balance. (Sally will always place the same number of coins on the right balance as on the left balance.) The word in the third position will tell whether the right side of the balance goes up, down, or remains even.

Output
For each case, the output will identify the counterfeit coin by its letter and tell whether it is heavy or light. The solution will always be uniquely determined.

Solution:
    find the balance of coins that are not even, and go through the coins to find the one not appeared in the rest comparison which are even
'''
if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        coins = []
        even = set()
        for n in range(3):
            c = list(map(str, input().split()))
            coins.append(c)
        fake, fake_row = None, None
        for i in range(3):
            if coins[i][2] == 'even':
                for a in str(coins[i][0]):
                    even.add(str(a))
                for b in str(coins[i][1]):
                    even.add(str(b))
            else:
                fake_row = i
        for a in str(coins[fake_row][0]):
            if a not in even:
                fake = a
        for b in str(coins[fake_row][1]):
            if b not in even:
                fake = b
        if coins[fake_row][2] == 'up':
            print(fake, "is the counterfeit coin and it is light.")
        else:
            print(fake, "is the counterfeit coin and it is heavy.")






