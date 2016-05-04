'''
Code

444 - Encoder and Decoder

The algorithm that you should use to encode messages is to take the ASCII value of each character in the message, starting with the last character in the message and ending with the first character in the message. You should then add on to the coded message this ASCII value written in reverse order. For example, if the ASCII value is 123, the encoded message should contain the string "321". There should be no spaces separating the numbers in the encoded message.
'''

while True:
    try:
        code = input()
        code = code[::-1]
        if ord(code[0]) in range(ord('0'), ord('9') + 1):
            for i in range(0, len(code), 2):
                n = code[i] + code[i+1]
                n = int(n)
                print(chr(n), end ="")
        else:
            for c in code:
                print(ord(c), end = "")
        print()
    except(EOFError):
        break
