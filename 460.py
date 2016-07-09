'''
Rectangle

460 - Overlapping Rectangles

When displaying a collection of rectangular windows on a SUN screen, a critical step is determining whether two windows overlap, and, if so, where on the screen the overlapping region lies.

Write a program to perform this function. Your program will accept as input the coordinates of two rectangular windows. If the windows do not overlap, your program should produce a message to that effect. If they do overlap, you should compute the coordinates of the overlapping region (which must itself be a rectangle).

All coordinates are expressed in "pixel numbers", integer values ranging from 0 to 9999. A rectangle will be described by two pairs of (X,Y) coordinates. The first pair gives the coordinates of the lower left-hand corner (XLL,YLL). The second pair gives the coordinates of the upper right-hand coordinates (XUR, YUR). You are guaranteed that XLL < XUR and YLL < YUR.
'''
if __name__ == '__main__':
    num = int(input())
    for i in range(num):
        if i > 0:
            print()
        empty = input()
        A, B, C, D = list(map(int, input().split()))
        E, F, G, H = list(map(int, input().split()))
        overlap = max(0, min(C, G) - max(A, E)) * max(0, min(D, H) - max(B, F))
        if overlap <= 0:
            print("No Overlap")
        else:
            print(max(A, E), max(B, F), min(C, G), min(D, H))




