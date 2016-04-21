'''
Set input - array
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
            setA = list(map(int, input().split()))
            setB = list(map(int, input().split()))
            memoA = set()
            diffA = set()
            memoB = set()
            diffB = set()
            isDisjoint = True
            for i in range(len(setA)):
                memoA.add(setA[i])
            for j in range(len(setB)):
                if setB[j] in memoA:
                    isDisjoint = False
                else:
                    diffA.add(setB[j])
            for i in range(len(setB)):
                memoB.add(setB[i])
            for j in range(len(setA)):
                if setA[j] in memoB:
                    isDisjoint = False
                else:
                    diffB.add(setA[j])
            if isDisjoint == True:
                print("A and B are disjoint")
            else:
                if len(diffA) == 0 and len(diffB) == 0:
                    print("A equals B")
                elif len(diffA) != 0 and len(diffB) == 0:
                    print("A is a proper subset of B")
                elif len(diffA) == 0 and len(diffB) != 0:
                    print("B is a proper subset of A")
                elif len(diffA) != 0 and len(diffB) != 0:
                    print("I'm confused!")
        except(EOFError):
            break



