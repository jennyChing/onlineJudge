def clear_above (blocks,i,j):
    for k in range(j+1, len(blocks[i])):
# blocks above blocks[i][j] move back to initial block
        blocks[blocks[i][k]].append(blocks[i][k])
# block list keep only blocks under blocks[i][j]
    if len(blocks[i]) > 1:
        blocks[i] = blocks[i][:j+1]
def move_onto (a,b):
    try:
        i_a, i_b = -1, -1
        j_a, j_b = -1, -1
        for i in range(0,n):
            for j in range(0,len(blocks[i])):
# locate the list and index in list that a located
                if blocks[i][j] == a:
                    i_a, j_a = i, j
                if blocks[i][j] == b:
                    i_b, j_b = i, j
# fix the clear_above function later
# if b and a are in the same block/list then rearrange a onto b
        if i_a == i_b:
            pass
        else:
            clear_above(blocks, i_a,j_a)
            clear_above(blocks, i_b,j_b)
            blocks[i_b].append(a)
            blocks[i_a].remove(a)
    except(IndexError):
        pass
def move_over (a,b):
    try:
        i_a, i_b = -1, -1
        j_a, j_b = -1, -1
        for i in range(0,n):
            for j in range(0,len(blocks[i])):
# locate the list and index in list that a located
                if blocks[i][j] == a:
                    i_a, j_a = i, j
                if blocks[i][j] == b:
                    i_b, j_b = i, j
# fix the clear_above function later
# if b and a are in the same block/list then rearrange a onto b
        if i_a == i_b:
            pass
# if a and b are not in the same block/list then remove a and insert to another list
        else:
            clear_above(blocks, i_a,j_a)
            blocks[i_b].append(a)
            blocks[i_a].remove(a)
#initialize all blocks above a and b
    except(IndexError):
        pass
def pile_onto (a,b):
    try:
        i_a, i_b = -1, -1
        j_a, j_b = -1, -1
        for i in range(0,n):
            for j in range(0,len(blocks[i])):
# locate the list and index in list that a located
                if blocks[i][j] == a:
                    i_a, j_a = i, j
                if blocks[i][j] == b:
                    i_b, j_b = i, j
# fix the clear_above function later
# if b and a are in the same block/list then rearrange a onto b
        if i_a == i_b:
            pass
# if a and b are not in the same block/list then remove and insert all a above together to list i_b
        else:
            clear_above(blocks, i_b,j_b)
            for k in range(j_a, len(blocks[i_a])):
               blocks[i_b].append(blocks[i_a][k])
            blocks[i_a] = blocks[i_a][:j_a]
#initialize all blocks above a and b
    except(IndexError):
       pass
def pile_over (a,b):
    try:
        i_a, i_b = -1, -1
        j_a, j_b = -1, -1
        for i in range(0,n):
            for j in range(0,len(blocks[i])):
# locate the list and index in list that a located
                if blocks[i][j] == a:
                    i_a, j_a = i, j
                if blocks[i][j] == b:
                    i_b, j_b = i, j
# if b and a are in the same block/list then rearrange a onto b
        if i_a == i_b:
            pass
# if a and b are not in the same block/list then remove and insert all a above together to list i_b
        else:
            for k in range(j_a, len(blocks[i_a])):
                blocks[i_b].append(blocks[i_a][k])
            blocks[i_a] = blocks[i_a][:j_a]
#initialize all blocks above a and b
    except(IndexError):
       pass
n_exist = False
if __name__ == "__main__":
    while True:
        try:
# read in the size of blocks
            if n_exist == False :
                n = int(input())
                n_exist = True
                blocks = [[] for _ in range(n)]
# set the blocks at their initial position
                for i in range(0,n):
                    blocks[i].append(i)
# read in the commands and call functions
            moves = list(map(str,input().split()))
            if moves[0] == "quit":
                break
            a = int(moves[1])
            b = int(moves[3])
# illiegal commands
            if a == b or a < 0 or b < 0 or a > 25 or b > 25:
                pass
            else:
                if moves[0] == "move" and moves[2] == "onto":
                    move_onto(a,b)
                if moves[0] == "move" and moves[2] == "over":
                    move_over(a,b)
                if moves[0] == "pile" and moves[2] == "onto":
                    pile_onto(a,b)
                if moves[0] == "pile" and moves[2] == "over":
                    pile_over(a,b)
        except(EOFError):break
for i in range(0,n):
    print(i,":",end="",sep="")
    if len(blocks[i]) == 1:
        print(" ",end="")
        print(blocks[i][0], end="")
    elif len(blocks[i]) > 1:
        print(" ",end="")
        for j in range(0,len(blocks[i])-1):
            print(blocks[i][j],end = " ")
        print(blocks[i][len(blocks[i])-1],end="")
    print()



