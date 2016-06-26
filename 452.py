'''
Topological Ordering

452 - Project Scheduling

Tasks A, B, C, D, E and F each take 5, 3, 2, 2, 4, and 2 days respectively, that task E cannot complete until C and D are both completed, but that D can be performed in parallel with B and C. Write a program that accepts a Pert chart and computes the amount of time required to complete a project.
'''
if __name__ == '__main__':
    case = int(input())
    empty = input()
    for _ in range(case):
        task_time = {}
        constrain = {}
        while True:
            try:
                content = list(map(str, input().split()))
            except(EOFError):
                print(task_time, constrain)
                break
            if len(content) == 0:
                print(task_time, constrain)
# use a graph to store the eligible paths
                MAXN = 26
                graph = [[ 0 for x in range(MAXN)] for y in range(MAXN)]
                char = []
                for k, v in task_time.items():
                    char.append(k)
                nodes = [ord(c[0]) - ord('A') for c in task_time.items()]
                nodes.sort()
                print(constrain)
                N = len(constrain) // 2
                for i in range(N):
                    print
                    graph[ord(constrain[i * 2 + 1]) - ord('A')][ord(constrain[i * 2]) - ord('A')] = 1
                print(graph)
# use kij algorithm to compute the reachability of all constraints
                for k in range(MAXN):
                    for i in range(MAXN):
                        for j in range(MAXN):
                            graph[i][j] |= (graph[i][k] & graph[k][j])
                N = len(nodes)
                print(graph)
                path = []
                used = [False] * N

# use DFS to traverse the graph and print whenever the len of nodes is reached(setp = N)
                def perm(step):
                    if step == N:
                        print (''.join(chr(p + ord('A')) for p in path))
                        return
                    for i in range(N):
# used[i] is False (node[i] is not used) and there is no contrains from node[i] to the rest of the path
                        if not used[i] and (step == 0 or all([graph[p][nodes[i]] == 0 for p in path])):
                            path.append(nodes[i])
                            used[i] = True
                            perm(step + 1)
                            path.pop()
                            used[i] = False
                perm(0)

                break
            task_time[content[0]] = content[1]
            if len(content) == 3:
                constrain[content[0]] = []
                for c in content[2]:
                    constrain[content[0]].append(c)



