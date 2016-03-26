'''
An algorithm given by Lothar Collatz produces sequences of integers, and is described as follows:
    Step 1: Choose an arbitrary positive integer A as the first item in the sequence.
    Step 2: If A = 1 then stop.
    Step 3: If A is even, then replace A by A/2 and go to step 2.
    Step 4: If A is odd, then replace A by 3 ∗ A + 1 and go to step 2.
'''
def seq(A, L, term):
    if A == 1:
        term += 1
        return term
    elif A > L:
        return term
    elif A%2 and A <= L:
        term += 1
        return seq(3*A+1, L, term)
    elif not A%2 and A <= L:
        term += 1
        return seq(A/2, L, term)

case = 0
if __name__ == '__main__':
    while True:
        case += 1
        value = list(map(int, input().split()))
        A, L = value[0], value[1]
        if A < 0 and L < 0:
            break
        term = 0
        print("Case ", case, ": A = ",A ,", limit = ", L, ", number of terms = ",seq(A, L, term),sep="")
