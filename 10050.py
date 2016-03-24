#def _gcd(a,b):
#    while b:
#        a, b = b, a % b
#    return a
#
#def _lcm(a,b):
#    return a*b // _gcd(a,b)  # // returns int
#
#def repeat(a, N):
## iteratively compute the lcm of two numbers from the set h
#    for i in range(0,len(a)-1):
#        for j in range(i+1,len(a)):
#            lcm = _lcm(a[i],a[j])
#            for k in range(1, 1+int(N/lcm)):
#                h.add(k*lcm)
#                print("lcm:",a[i],a[j],lcm)
#                print("delete:",h)
#    if N >= 6:
#        rest.append(6)
#    if N >=7:
#        for i in range(1,N//7):
#            rest.append(i*7)
#            rest.append(i*7-1)
#            print("delete:",h)

T = int(input()) # of cases
if __name__ == '__main__':
    while True:
        try:
            for i in range(0,T):
                N = int(input()) # of days
                P = int(input()) # of political parties
                a = [] # hartal parameter
                fac =set() # store all eligible factors
# record all the hartal parameters
                for i in range(0,P):
                    h = int(input())
                    a.append(h)
# record all factors (if itself and +1 both not multiple of 7) and multiples under N in a set, the hartals would be the len of these factors
                for i in range(0,P):
                    for j in range(1, 1+N//a[i]):
                        if a[i]*j%7!=0 and (a[i]*j+1)%7!=0 and a[i]*j!=6:
                            fac.add(a[i]*j)
                print(len(fac))
            break
        except(EOFError):
            break
