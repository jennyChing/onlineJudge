'''
483 Word Scramble:
Write a program that will reverse the letters in each of a sequence of words while preserving the order of the words themselves.
'''
if __name__ == '__main__':
    while True:
        try:
            content = input()
            content = content+" "
            a = 0
            b = 0
            isWord = False
            for i in range(0,len(content)):
                if content[i] == " " and isWord == True:
                    b = i
                    isWord = False
                    print(content[b:a-1:-1],end="")
                elif content[i] != " " and isWord == False:
                    a = i
                    isWord = True
                if content[i] == " ":
                    print(" ", end="")
            print()
        except(EOFError):
            break
