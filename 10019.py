'''
10019 - Funny Encryption Method
1. Read the number N to encrypt : M = 265
2. Interpret N as a decimal number : X1 = 265 (decimal)
3. Convert the decimal interpretation of N to its binary representation : X1 = 100001001 (binary)
4. Let b1 be equal to the number of 1’s in this binary representation : b1 = 3
5. Interpret N as a Hexadecimal number : X2 = 265 (hexadecimal)
6. Convert the hexadecimal interpretation of N to its binary representation : X2 = 1001100101
7. Let b2 be equal to the number of 1’s in the last binary representation : b2 = 5
8. The encryption is the result of M xor (b1 ∗ b2) : 265 xor (3*5) = 262
This student failed Computational Organization, thats why this student asked the judges of ITESM
Campus Monterrey internal ACM programming Contest to ask for the numbers of 1’s bits of this two representations so that he can continue playing. You have to write a program that read a Number and give as output the number b1 and b2
'''
cases = int(input())
for n in range(cases):
    m = int(input())
    b1, b2 = 0, 0
    lst_b1 = bin(m)
    for c in lst_b1:
        if c == '1':
            b1 += 1
    m = str(m)
    lst_b2 = bin(int(m, 16))
    for c in lst_b2:
        if c == '1':
            b2 += 1
    print(b1, b2)

