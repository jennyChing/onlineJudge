'''
Palindrome

10945 - Mother bear

Input
You’ll be given many sentences. You have to determine if they are palindromes or not, ignoring case and punctuations. Every sentence will only contain the letters A-Z, a-z, ‘.’, ‘,’, ‘!’, ‘?’. The end of input will be a line containing the word ‘DONE’, which should not be processed.

Output
On each input, output ‘You won’t be eaten!’ if it is a palindrome, and ‘Uh oh..’ if it is not a palindrome.
'''
if __name__ == '__main__':
    while True:
        try:
            content = input()
            if content == 'DONE':
                break
            alphas = []
            for c in content:
                if c.isalpha() == True:
                    c = c.lower()
                    alphas.append(c)
            isPal = True
            for i in range(0, len(alphas)//2):
                if alphas[i] != alphas[len(alphas) - i - 1]:
                    print("Uh oh..")
                    isPal = False
                    break
            if isPal != False:
                print("You won’t be eaten!")
        except(EOFError):
            break
