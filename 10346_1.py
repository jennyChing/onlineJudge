def calCigar(lst, cigar, n, k):
    if n >= k:
        cigar = cigar + n//k
# append cigar into lst first then call the recursive calCigar function
        lst.append(cigar)
        calCigar(lst, cigar, n%k+n//k, k)
    return lst[-1]
if __name__ == "__main__":
    while True:
        try:
            value = list(map(int, input().split()))
            n = value[0]
            k = value[1]
            cigar = n
            lst = []
            print(calCigar(lst, cigar, n, k))
        except(EOFError):
            break
