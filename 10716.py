'''
Palindrome

10716 - Evil Straw Warts Live

Input
The first line of input gives n, the number of test cases. For each test case, one line of input follows, containing a string of up to 100 lowercase letters.

Output
Output consists of one line per test case. This line will contain the number of swaps, or ‘Impossible’ if it is not possible to transform the input to a palindrome.
'''
if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        alpha_arr = []
        alpha_dict = {}
        content = input()
        for c in content:
            alpha_arr.append(c)
            if c in alpha_dict:
                alpha_dict[c] += 1
            else:
                alpha_dict[c] = 1
        isImp, hasOdd = False, False
        for k, v in alpha_dict.items():
            if hasOdd == True and v % 2 == 1:
                isImp = True
                print("Impossible")
                break
            elif hasOdd == False and v % 2 == 1:
                hasOdd = True
        if isImp != True:
            print(alpha_arr)
