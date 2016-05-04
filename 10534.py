'''
Longest increasing string

10534 - Wavio Seq

Wavio is a sequence of integers. It has some interesting properties.
• Wavio is of odd length i.e. L = 2 ∗ n + 1.
• The first (n + 1) integers of Wavio sequence makes a strictly increasing sequence.
• The last (n + 1) integers of Wavio sequence makes a strictly decreasing sequence.
• No two adjacent integers are same in a Wavio sequence.
For example 1, 2, 3, 4, 5, 4, 3, 2, 0 is an Wavio sequence of length 9. But 1, 2, 3, 4, 5, 4, 3, 2, 2 is not a valid wavio sequence. In this problem, you will be given a sequence of integers. You have to find out the length of the longest Wavio sequence which is a subsequence of the given sequence. Consider, the given sequence as :
    1 2 3 2 1 2 3 4 3 2 1 5 4 1 2 3 2 2 1.
    Here the longest Wavio sequence is : 1 2 3 4 5 4 3 2 1. So, the output will be ‘9’.
Solution:
    LIS x2 times: from left to right and right to left => use the smaller value from the 2 results to calculate the LIS
'''
if __name__ == '__main__':
    while True:
        try:
            seq = list(map(int, input().split()))
            N = seq[0]
            nums = seq[1:]
            n_cnt = len(seq) - 1
            while n_cnt < N:
                seq = list(map(int, input().split()))
                n_cnt += len(seq)
                nums += seq
                print(n_cnt, nums)
            print(nums)
            longest_inc = [1] * N
            longest_drc = [1] * N
            #for i in range(len(seq)):
            #    for j in range(i + 1, len(seq)):
            #        if seq[j] > seq[i]:
            #            longest_inc[i] += 1
            #        else:
            #            break
            #for i in range(len(seq)):
            #    for j in range(i + 1, len(seq)):
            #        if seq[j] < seq[i]:
            #            longest_drc[i] += 1
            #        else:
            #            break
            #print(longest_inc, longest_drc)
            #isWavio = 1
            #for i in range(N):
            #    for j in range(i, N):
            #        temp = min(longest_drc[longest_inc[i] + i - 1], longest_inc[i])
            #        if temp > isWavio:
            #            isWavio = 2 * temp - 1
            #print(isWavio)
        except(EOFError):
            break

