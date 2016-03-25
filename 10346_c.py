class calCigar(object):
    def __init__ (self,n,k):
        self.n = n
        self.k = k
        self.cigar = self.n

    def devide (self):
        return self.n//self.k

    def sumCigar (self):
        # self.n cannot be modified??
        while self.n//self.k > self.k:
            self.n = self.n//self.k
            print(self.n)
            self.cigar = self.cigar + self.n
        return self.cigar

if __name__ == '__main__':
    while True:
        try:
            c = calCigar(100,5)
            print(c.sumCigar())
        except(EOFError):
            break

