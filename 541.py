'''
541 - Error Correction
A boolean matrix has the parity property when each row and each column has an even sum, i.e. contains an even number of bits which are set. Here's a 4 x 4 matrix which has the parity property:
    1 0 1 0
    0 0 0 0
    1 1 1 1
    0 1 0 1
    The sums of the rows are 2, 0, 4 and 2. The sums of the columns are 2, 2, 2 and 2.  Your job is to write a program that reads in a matrix and checks if it has the parity property. If not, your program should check if the parity property can be established by changing only one bit. If this is not possible either, the matrix should be classified as corrupt.
'''
while True:
    try:
        matrix = []
        sum_row, sum_col = [], []
        c_row, c_col = None, None
        isBreak = False
# read the size n of the matrix
        n = int(input())
        if n == 0:
            break
# read in next n rows of input as the value of the matrix
        for i in range(n):
            row = list(map(int, input().split()))
            matrix.append(row)
            x = sum(row)
            if x % 2 and isBreak == False:
                if not c_row:
                    c_row = i + 1
                else:
                    isBreak = True
                    print("Corrupt")
            sum_row.append(x)
        if isBreak == False:
            for i in range(n):
                x = sum(j[i] for j in matrix)
                if x % 2:
                    if not c_col:
                        c_col = i + 1
                    else:
                        print("Corrupt")
                        isBreak = True
                sum_col.append(x)
        if isBreak == False:
            if not c_row and not c_col:
                print("OK")
            elif c_row != None and c_col != None:
                print("Change bit (", c_row, ",", c_col,")",sep = "")
    except(EOFError):
        break

