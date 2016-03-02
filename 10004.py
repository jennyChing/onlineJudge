def colorify(color,i, C1, C2):
    color[i] = C1
    for j in range(0, nodes):
        if color[j] == color[j-1]:
            possible = False
        if color[j] == 0:
            colorify(color,j, C2, C1)
            print("here",color)
            print(color[j])
def DFS(color,i): # v is the vertex where the search starts
    #S = {} #start with an empty stack
    for j in range(0, nodes):
        if visit[j] == False and adj_matrix[i][j] == True:
            visit[j] = True
            colorify(color, j, "BLACK", "WHITE")
            DFS(color,j)
            print("i:",i,"j:",j)
if __name__ == '__main__':
    while True:
        try:
            possible = True
            nodes = int(input())
            if nodes ==0:
                break
            adj_matrix = [[0 for x in range(nodes)] for x in range(nodes)]
            visit = [False for x in range(nodes)]
            color = [0 for x in range(nodes)]
            edges = int(input())
            for i in range(0, edges):
                edge_list = list(map(int, input().split()))
                start = edge_list[0]
                end = edge_list[1]
                adj_matrix[start][end] = 1
                adj_matrix[end][start] = 1
            print(visit,adj_matrix)
            for i in range(1,nodes+1):
                if visit[i] == False:
                    visit[i] = True
                    DFS(color,i)
            if possible == True:
                print("BICOLORABLE.")
            else:
                print("NOT BICOLORABLE.")
        except(EOFError):
            break

