if __name__ == '__main__':
    while True:
        try:
            ID = list(input())
            if ID == ['#']:
                break
            i = len(ID) - 1 # pointer of checking descendence
            start, exchange = None, None
            while i > 0:
                if ID[i - 1] < ID[i]:
                    start = i - 1
                    break
                i += -1
            if start == None:
                print("No Successor")
                continue
            right = ID[start + 1:]
            for c in range(len(right)):
                if ord(ID[start]) < ord(right[c]):
                    exchange = start + 1 + c
            ID[start], ID[exchange] = ID[exchange], ID[start]
            ID[start + 1:] = ID[start + 1:][::-1]
            for i in ID:
                print(''.join(i), end = "")
            print()
        except(EOFError):
            break

