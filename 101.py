def clear_above (blocks,i,j):
    for k in range(j+1, len(blocks[i])):
# blocks above blocks[i][j] move back to initial block
        blocks[k].append(k)
# block list keep only blocks under blocks[i][j]
    blocks[i] = blocks[i][:j]
def move_onto (a,b):
    try:
        i_a, i_b = -1, -1
        j_a, j_b = -1, -1
        for i in range(0,n):
            for j in range(0,n):
# locate the list and index in list that a located
                print(blocks[i][j],a)
                if blocks[i][j] == a:
                    i_a, j_a = i, j
                if blocks[i][j] == b:
                    i_b, j_b = i, j
#initialize all blocks above a and b
                clear_above(blocks, i_a,j_a)
                clear_above(blocks, i_b,j_b)
# if b and a are in the same block/list then rearrange a onto b
                if i_a == i_b:
                    blocks[i_a].insert(j_b,a)
                    blocks[i_a].remove(a)
# if a and b are not in the same block/list then remove a and insert to another list
                else:
                    blocks[i_b].insert(j_b,a)
                    blocks[i_a].remove(a)
    except(IndexError):
       pass
n_exist = False
if __name__ == "__main__":
    while True:
        try:
# read in the size of blocks
            if n_exist == False :
                n = int(input())
                n_exist == True
                print(n_exist)
                blocks = [[None for x in range(n)] for x in range(n)]
                print(blocks)
# set the blocks at their initial position
                for i in range(0,n):
                    blocks[i][0] = i
                print(blocks)
# read in the commands and call functions
            moves = list(map(str,input().split()))
            if moves[0] == "quit":
                break
            a = int(moves[1])
            b = int(moves[3])
            print(type(a), type(b),moves)
# illiegal commands
            if a == b or a < 0 or b < 0 or a > 25 or b > 25:
                pass
            else:
                if moves[0] == "move" and moves[2] == "onto":
                    move_onto(a,b)
            print(blocks)
        except(EOFError):break



