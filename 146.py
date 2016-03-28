if __name__ == '__main__':
    while True:
        try:
            ID = list(input())
            if ID == ['#']:
                break
            i = len(ID) - 1 # pointer of checking descendence
            j = -1 # right remaining parts that need sorting is ID[j+1:]
            start, exchange = None, None
            while i > 0:
                if ID[i-1] < ID[i]:
                    j = i-1
                    start = j
                    break
                i += -1
            right_min = float("inf")
            right = ID[j+1:]
            for c in range(len(right)):
                if right_min > ord(right[c]):
                    right_min = ord(right[c])
                    exchange = j + 1 + c
            if start != None and exchange != None:
                ID[start], ID[exchange] = ID[exchange], ID[start]
                ID[start + 1:] =  sorted(ID[start + 1:])
                for i in ID:
                    print(''.join(i),end="")
                print()
            else:
                print("No Successor")
        except(EOFError):
            break

