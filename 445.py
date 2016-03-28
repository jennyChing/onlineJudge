'''
445 - Marvelous Mazes
The lowercase letter "b" will be used in the input file to represent spaces in the maze. The descriptions for different rows in the maze will be separated by an exclamation point (!) or by an end of line.

T TTTTT
T  T TT
T T  TT
T   T T
TTT   T
T   T T
TTTTT*T
'''
if __name__ == '__main__':
    while True:
        try:
            content = list(input())
            isNum = True
            repeat = 0
            for i in range(len(content)):
                if content[i] == '!':
                    print()
                else:
                    try:
                        content[i] = int(content[i])
                        repeat += content[i]
                    except(ValueError):
                        isNum = False
                        if content[i] == 'b':
                            print(" "*repeat, end="")
                        else:
                            print(content[i]*repeat, end="")
                        repeat = 0
                        pass
            print()

        except(EOFError):
            break
