'''
In the last IIUPC there was a problem called Da Vinci Code prepared on the story of the bestselling book of Dan Brown, The Da Vinci Code. Here is another problem based on his another techno-thriller novel Digital Fortress. In this problem, you will be given a cipher text. Your task is to decipher the text using the decrypting technique described below. Let’s take an example. A cipher text is given as
follows:

    WECGEWHYAAIORTNU

The output will be:

    WEAREWATCHINGYOU

For this problem, there are 16 characters in the given cipher text “WECGEWHYAAIORTNU” which is square of 4. These letters have to be arranged in n×n (in this example 4×4) grid and each letter from the given input will be placed in a grid in row major order (1st row, 2nd row, 3rd row, ...). When the given cipher text is placed in the grid it looks like as follow:
    W E C G
    E W H Y
    A A I O
    R T N U
From the above grid if we take the letters in column major order (1st column, 2nd column, 3rd column, ...) then we get the following decrypted text:

    WEAREWATCHINGYOU
'''
cases = int(input())
while True:
    try:
        word = input()
        N = len(word)**(0.5)
        if N % 1 == 0:
            for i in range(int(N)):
                for j in range(int(N)):
                    print(word[i + j * int(N)], end = "")
            print()
        else:
            print("INVALID")
    except(EOFError):
        break
