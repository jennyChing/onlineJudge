def DFS(i): # v is the vertex where the search starts
    for j in range(0, nodes):
        if adj_matrix[i][j] == True:
            #print("i:",i,"j:",j,"/color[i]:",color[i],"/color[j]:",color[j],"/visit[i]:",visit[i],"/visit[j]:",visit[j])
            if visit[j] == True and color[j] == color[i]:
                return False
            if visit[j] == False:
                visit[j] = True
                color[j] = True if color[i]==False else False
                if DFS(j) == False:
                    return False
    return True
if __name__ == '__main__':
    while True:
        try:
            nodes = int(input())
            if nodes ==0:
                break
            adj_matrix = [[ False for x in range(nodes)] for x in range(nodes)]
            visit = [False for x in range(nodes)]
            color = [None for x in range(nodes)]
            edges = int(input())
            for i in range(0, edges):
                edge_list = list(map(int, input().split()))
                start = edge_list[0]
                end = edge_list[1]
                adj_matrix[start][end] = True
                adj_matrix[end][start] = True
            #print(visit,adj_matrix)
            possible = True
            for i in range(0,nodes):
                if visit[i] == False:
                    visit[i] = True
                    color[i] = True
                    if DFS(i) == False:
                        print("NOT BICOLORABLE.")
                        possible = False
                        break
            if possible == True:
                print("BICOLORABLE.")
        except(EOFError):
            break

