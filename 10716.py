'''
Palindrome

10716 - Evil Straw Warts Live

Input
The first line of input gives n, the number of test cases. For each test case, one line of input follows, containing a string of up to 100 lowercase letters.

Output
Output consists of one line per test case. This line will contain the number of swaps, or ‘Impossible’ if it is not possible to transform the input to a palindrome.
'''
def cal_swaps(alpha_index_dict, alpha_arr, target, actual):
    swaps = abs(target - actual)
    if target > actual:
        alpha_arr = alpha_arr[:actual] + [alpha_arr[target]] + alpha_arr[actual:target] + alpha_arr[target + 1:]
        alpha_index_dict

    else:
        alpha_arr = alpha_arr[:target] + [alpha_arr[actual]] + alpha_arr[target:actual] + alpha_arr[actual + 1:]
    return swaps, alpha_arr, alpha_index_dict

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        alpha_arr = []
        alpha_index_dict = {}
        content = input()
        for i in range(len(content)):
            alpha_arr.append(content[i])
            if content[i] in alpha_index_dict:
# a hash table storing the indexes of each character to be used as future target index (NOT GOOD since we need to change the index after every swap)
                alpha_index_dict[content[i]].append(i)
            else:
                alpha_index_dict[content[i]] = [i]
        isImp, hasOdd = False, False
        swaps, middle = None, None
        for k, v in alpha_index_dict.items():
            if hasOdd == True and len(v) % 2 == 1:
                isImp = True
                print("Impossible")
                break
            elif hasOdd == False and len(v) % 2 == 1:
                middle = k
                hasOdd = True
        if isImp != True:
# start checking from the middle!
            for i in range(len(alpha_arr)):
                if middle != None and alpha_arr[i] == middle:
                    swaps, alpha_arr, alpha_index_dict = cal_swaps(alpha_index_dict, alpha_arr, len(alpha_arr)//2, i)
                    print(i, swaps, alpha_arr)
            print(alpha_index_dict)
# then check the two sides of the alpha_arr (use swaps that are minimized)
            for i in range(len(alpha_arr)):
                if alpha_arr[i] != alpha_arr[len(alpha_arr) - i - 1]:
                    left, right = i, len(alpha_arr) - i - 1
                    print(alpha_arr[i], alpha_index_dict[alpha_arr[i]], left, right)
                    swaps, alpha_arr, alpha_index_dict = cal_swaps(alpha_index_dict, alpha_arr, alpha_index_dict[alpha_arr[left]][0], alpha_index_dict[alpha_arr[right]][1])
            print(alpha_index_dict)

