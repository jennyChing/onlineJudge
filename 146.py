def check(ID):
    ID_copy = ID
    print(ID)
    for i in range(len(ID)-1):
        for j in range(len(ID)-1):
            print(ID[i],ID[j])
            if ord(ID[i]) > ord(ID[j]):
                temp = ID[i]
                temp2 = ID[j]
                ID[i] = temp2
                ID[j] = temp
                print("yes:",ID[i], ID[j])
    if ID_copy == ID:
        return "No Successor"

if __name__ == '__main__':
    while True:
        try:
            ID = list(input())
            if ID == ['#']:
                break
            ID = ID[::-1]
            print(check(ID))
        except(EOFError):
            break

