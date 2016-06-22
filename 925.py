'''
Topological Sort

200 - Rare Order

You are to write a program to complete the collector’s work. In particular, your program will take a set of strings that has been sorted according to a particular collating sequence and determine what that sequence is.

Sample Input
XWY
ZX
ZXY
ZXW
YWWX
#
Sample Output => the new letter order that the input is based on
XZYW
'''
if __name__ == '__main__':
    words = []
    while True:
        w = input()
        if w == '#':
            break
        words.append(w)
    print(words)
