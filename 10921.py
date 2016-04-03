'''
10921 - Find the Telephone
In some places is common to remember a phone number associating its digits to letters. In this way
the expression “MY LOVE” means 69 5683. Of course there are some problems, because some phone numbers can not form a word or a phrase and the digits 1 and 0 are not associated to any letter.  Your task is to read an expression and find the corresponding phone number based on the table below. An expression is composed by the capital letters (A-Z), hyphens (-) and the numbers 1 and 0.  Letters Number ABC 2 DEF 3 GHI 4 JKL 5 MNO 6 PQRS 7 TUV 8 WXYZ 9
'''
d = {}
w = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
for k, v in zip(w, range(2, 10)):
    for c in k:
        d[c] = str(v)
d['0'] = '0'
d['1'] = '1'
d['-'] = '-'
while True:
    try:
        word = input()
        for c in word:
            if c in d:
                print(d[c], end = "")
            elif c == ' ':
                print()
        print()
    except(EOFError):
        break
