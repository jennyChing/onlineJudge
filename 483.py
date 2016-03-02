def reverse (content,a,b):
    word=[]
    for i in range(a,b):
        word.append(content[i])
    print(''.join(word[::-1]),end="")
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
                    reverse(content,a,b)
                elif content[i] != " " and isWord == False:
                    a = i
                    isWord = True
                if content[i] == " " and i < len(content)-1:
                    print(" ", end="")
            print()
        except(EOFError):
            break
