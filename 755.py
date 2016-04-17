'''
Sort - QuickSort
755 - 487--3279

The standard form of a telephone number is seven decimal digits with a hyphen between the third and fourth digits (e.g. 888–1200). The keypad of a phone supplies the mapping of letters to numbers, as follows:
    A, B, and C map to 2
    D, E, and F map to 3
    G, H, and I map to 4
    J, K, and L map to 5
    M, N, and O map to 6
    P, R, and S map to 7
    T, U, and V map to 8
    W, X, and Y map to 9
    There is no mapping for Q or Z. Hyphens are not dialed, and can be added and removed as necessary.  The standard form of TUT–GLOP is 888–4567, the standard form of 310–GINO is 310–4466, and the standard form of 3–10–10–10 is 310–1010.
    Two telephone numbers are equivalent if they have the same standard form. (They dial the same number.) Your company is compiling a directory of telephone numbers from local businesses. As part of the quality control process you want to check that no two (or more) businesses in the directory have the same telephone number.
'''
memo = {'A': 2, 'B': 2, 'C': 2, 'D': 3, 'E': 3, 'F': 3, 'G': 4, 'H': 4, 'I': 4, 'J': 5, 'K': 5, 'L': 5, 'M': 6, 'N': 6, 'O': 6, 'P': 7, 'R': 7, 'S': 7, 'T': 8, 'U': 8, 'V': 8, 'W': 9, 'X': 9, 'Y': 9}
if __name__ == '__main__':
    cases = int(input())
    for case in range(cases):
        if case > 0:
            print("")
        blank = input()
        N = int(input())
        phones = {}
        for n in range(N):
            p = input()
            phone = ""
            for c in p:
                if c in memo:
                    phone += str(memo[c])
                elif c != '-':
                    phone += c
            if phone in phones:
                phones[phone] += 1
            else:
                phones[phone] = 1
        sorted_p = sorted(phones)
        isDuplicate = False
        for p in sorted_p:
            if phones[p] > 1:
                isDuplicate = True
                print(p[:3], '-', p[3:], " ", phones[p], sep = "")
        if isDuplicate == False:
            print("No duplicates.")
