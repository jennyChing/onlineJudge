'''
functions -

350 - Pseudo-Random Numbers

A common pseudo-random number generation technique is called the linear congruential method. If the last pseudo-random number generated was L, then the next number is generated by evaluating ( tex2html_wrap_inline32 , where Z is a constant multiplier, I is a constant increment, and M is a constant modulus. For example, suppose Z is 7, I is 5, and M is 12.

In this problem you will be given sets of values for Z, I, M, and the seed, L. Each of these will have no more than four digits. For each such set of values you are to determine the length of the cycle of pseudo-random numbers that will be generated. But be careful: the cycle might not begin with the seed!
'''
def mod(Z, I, M, L):
    remain = (Z * L + I) % M
    if remain in seen:
        return seen
    seen.add(remain)
    mod(Z, I, M, remain)

case = 0
if __name__ == '__main__':
    while True:
        try:
            Z, I, M, L = list(map(int, input().split()))
            if Z == 0 and I == 0 and M == 0 and L == 0:
                break
            elif M == 0:
                continue
            while L > M:
                L = L % M
            case += 1
            seen = set()
            mod(Z, I, M, L)
            print("Case ", case, ": ", len(seen), sep="")
        except(EOFError):
            break
