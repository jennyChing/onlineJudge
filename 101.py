def clear_above (i,j):
    if j<n:
        for j in range(j,n):
            value = blocks[i][j]
            blocks[value][0] = value
            blocks[i][j] = -1
def move_onto (a,b):
    try:
        i_a = -1
        i_b = -1
        j_a = -1
        j_b = -1
        for i in range(0,n):
            for j in range(0,n):
                if blocks[i][j] == a:
                    i_a = i
                    j_a = j
                    blocks[i] =
                if b in blocks[i]:
                    blocks[i].append(a)
                    blocks[a].remove(a)
    except(IndexError):
       pass
n_exist = False
if __name__ == "__main__":
    while True:
        try:
            if n_exist == False :
                n = int(input())
                n_exist == True
            blocks = {}
            print(blocks)
            for i in range(0,n):
                blocks[i] = i
            print(blocks)
            moves = list(map(str,input().split()))
            if moves[0] == "quit":
                break
            a = int(moves[1])
            b = int(moves[3])
            if a ==b or a < 0 or b < 0 or a > 25 or b > 25:
                pass
            else:
                if moves[0] == "move" and moves[2] == "onto":
                    move_onto(a,b)
            print(blocks)
        except(EOFError):break



