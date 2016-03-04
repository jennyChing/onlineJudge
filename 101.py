#def move_onto (a,b):

if __name__ == "__main__":
    while True:
        try:
            n = int(input())
            blocks = [[False for i in range(0,n)] for i in range(0,n)]
            print(blocks)
            for i in range(0,n):
                blocks[i] = i
            print(blocks)
        except(EOFError):break
