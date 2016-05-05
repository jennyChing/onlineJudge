'''
Code

444 - Encoder and Decoder

The algorithm that you should use to encode messages is to take the ASCII value of each character in the message, starting with the last character in the message and ending with the first character in the message. You should then add on to the coded message this ASCII value written in reverse order. For example, if the ASCII value is 123, the encoded message should contain the string "321". There should be no spaces separating the numbers in the encoded message.
'''
while True:
    try:
        code = input()
    except(EOFError):
        break
    if len(code) == 0:
        print()
    else:
        if ord(code[0]) in range(ord('0'), ord('9') + 1):
            code = code[::-1]
            result = []
            while len(code) > 0:
                if int(code[0: 0 + 3]) in (range(100, 123)):
                    c = chr(int(code[0:0 + 3]))
                    code = code[3:]
                else:
                    c = chr(int(code[0:0 + 2]))
                    code = code[2:]
                result.append(c)
            print (''.join(result))
        else:
            result = []
            for c in code:
                result.append(str(ord(c)))
            result = ''.join(result)
            print(result[::-1])
