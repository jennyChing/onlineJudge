'''
Set - array
496 - Simply Subsets

Input

Your program should accept an even number of lines of text. Each pair of lines will represent two sets; the first line represents set A, the second line represents set B. Each line of text (set) will be a list of distinct integers.

Output

After each pair of lines has been read in, the sets should be compared and one of the following responses should be output:

    A is a proper subset of B
    B is a proper subset of A
    A equals B
    A and B are disjoint
    I'm confused! 部分重疊
'''
if __name__ == '__main__':
    while True:
        try:
            A = list(map(int, input().split()))
            B = list(map(int, input().split()))
            a = A & B
            if A == B:
                print("A equals B")
            elif a == A:
                print("A is a proper subset of B")
            elif a == B:
                print("B is a proper subset of A")
            elif not a:
                print("A and B are disjoint")
            else:
                print("I'm confused!")
        except(EOFError):
            break



