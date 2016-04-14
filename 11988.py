'''
Data - list
11988 - Broken Keyboard (a.k.a. Beiju Text)

Input

There are several test cases. Each test case is a single line containing at least one and at most 100,000 letters, underscores and two special characters ‘[’ and ‘]’. ‘[’ means the “Home” key is pressed internally, and ‘]’ means the “End” key is pressed internally. The input is terminated by end-of-file (EOF).

Output

For each case, print the Beiju text on the screen.
'''
if __name__ == '__main__':
    while True:
        try:
            text = input()
# text to be printed
            array = []
# keep track of the [] pairs
            pairs = []
# store the text in [] that need to be print first
            temp = []
            for c in text:
                if c == '[':
                    pairs.append('[')
                elif c == ']':
                    try:
                        pairs.pop()
                    except(IndexError):
                        continue
                    for i in range(len(temp)):
                        array.insert(0, temp[i])
                    temp = []
                elif len(pairs) == 0:
                    array.append(c)
                else:
                    temp.insert(0, c)
            for i in range(len(array)):
                print(array[i], end ="")
            print()
        except(EOFError):
            break

