'''
10106 Product:
The problem is to multiply two integers X, Y . (0 ≤ X, Y < 10250)
'''
while True:
    try:
        for i in range(2):
            a = int(input())
            b = int(input())
            print(a*b)
    except(EOFError):
        break

