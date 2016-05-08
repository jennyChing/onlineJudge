'''
Binary Heap

501 - Black Box

• ADD(x): put element x into Black Box;
• GET: increase i by 1 and give an i-minimum out of all integers containing in the Black Box.

1. A(1), A(2), . . . , A(M): a sequence of elements which are being included into Black Box. A values are integers not exceeding 2 000 000 000 by their absolute value, M ≤ 30000 . For the Example we have A = (3, 1, −4, 2, 8, −1000, 2).
2. u(1), u(2), . . . , u(N) : a sequence setting a number of elements which are being included into Black Box at the moment of first, second, ... and N-transaction GET. For the Example we have
u = (1, 2, 6, 6).

For each dataset, write to the output Black Box answers sequence for a given sequence of transactions
'''
if __name__ == '__main__':
    while True:
        try:
            case = int(input())
            for i in range(case):
                if i > 0:
                    print()
                blank = input()
                blank = input()
                A = list(map(int, input().split()))
                u = list(map(int, input().split()))
                for j in range(len(u)):
                    temp = A[:u[j]]
                    print(sorted(temp)[j])
        except(EOFError):
            break

