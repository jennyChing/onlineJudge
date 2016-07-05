'''
Rectangle

460 - Overlapping Rectangles

When displaying a collection of rectangular windows on a SUN screen, a critical step is determining whether two windows overlap, and, if so, where on the screen the overlapping region lies.

Write a program to perform this function. Your program will accept as input the coordinates of two rectangular windows. If the windows do not overlap, your program should produce a message to that effect. If they do overlap, you should compute the coordinates of the overlapping region (which must itself be a rectangle).

All coordinates are expressed in "pixel numbers", integer values ranging from 0 to 9999. A rectangle will be described by two pairs of (X,Y) coordinates. The first pair gives the coordinates of the lower left-hand corner (XLL,YLL). The second pair gives the coordinates of the upper right-hand coordinates (XUR, YUR). You are guaranteed that XLL < XUR and YLL < YUR.
'''
if __name__ == '__main__':
    while True:
        try:
            num = int(input())
        except(EOFError):
            break
        empty = input()
        w1 = list(map(int, input().split()))
        w2 = list(map(int, input().split()))
        print(w1, w2)
        if w1[3] > w2[3] and w1[1] > w1[1]:
            print(w1[3])
            u, d = w2[3], w1[1]
        elif w1[3] < w2 [3] and w1[1] < w1[1]:
            d, u = w2[3], w1[1]
        if w1[2] > w2 [2] and w1[0] > w1[0]:
            r, l = w2[2], w1[1]
        elif w1[2] < w2 [2] and w1[0] < w1[0]:
            l, r = w2[2], w1[0]
        try:
            print(l, d, r, u)
        except(NameError):
            print("No Overlap")




