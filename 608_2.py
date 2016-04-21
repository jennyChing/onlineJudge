'''
set search - array
608 - Counterfeit Dollar

Sally Jones has a dozen Voyageur silver dollars. However, only eleven of the coins are true silver dollars; one coin is counterfeit even though its color and size make it indistinguishable from the real silver dollars. The counterfeit coin has a different weight from the other coins but Sally does not know if it is heavier or lighter than the real coins.

Input
The first line of input is an integer n (n > 0) specifying the number of cases to follow. Each case consists of three lines of input, one for each weighing. Sally has identified each of the coins with the letters A–L. Information on a weighing will be given by two strings of letters and then one of the words “up”, “down”, or “even”. The first string of letters will represent the coins on the left balance; the second string, the coins on the right balance. (Sally will always place the same number of coins on the right balance as on the left balance.) The word in the third position will tell whether the right side of the balance goes up, down, or remains even.

Output
For each case, the output will identify the counterfeit coin by its letter and tell whether it is heavy or light. The solution will always be uniquely determined.

Solution:
    if not even, count the appearance of each coins and return the one apeared the most (exclude all the coins apeared in even)
'''
if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        left = [0] * 12
        right = [0] * 12
        even = set()
        isUp, isDown = 0, 0
        for n in range(3):
            c = list(map(str, input().split()))
            if c[2] == 'up':
                isUp = 1
            if c[2] != 'even':
                for a in str(c[0]):
                    left[ord(a) - ord('A')] += 1
                for b in str(c[1]):
                    right[ord(b) - ord('A')] += 1
            else:
                for a in str(c[0]):
                    even.add(a)
                for b in str(c[1]):
                    even.add(b)
        max_c, max_i = 0, 0
        print(left, right)
        for i, v in enumerate(left):
            if v > max_c and chr(i + ord('A')) not in even:
                max_c = v
                max_i = i
                #isUp = isUp * -1
        for i, v in enumerate(right):
            if v > max_c and chr(i + ord('A')) not in even:
                max_c = v
                max_i = i
        fake = chr(ord('A') + max_i)
        if isUp == 1:
            print(fake, "is the counterfeit coin and it is heavy.")
        else:
            print(fake, "is the counterfeit coin and it is light.")
