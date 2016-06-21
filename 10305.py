'''
Topological Ordering

10305 - Ordering Tasks

Input
The input will consist of several instances of the problem. Each instance begins with a line containing two integers, 1 ≤ n ≤ 100 and m. n is the number of tasks (numbered from 1 to n) and m is the number of direct precedence relations between tasks. After this, there will be m lines with two integers i and j, representing the fact that task i must be executed before task j.  An instance with n = m = 0 will finish the input.

Output
For each instance, print a line with n integers representing the tasks in a possible order of execution.
'''
if __name__ == '__main__':
    while True:
        n, m = list(map(int, input().split()))
        if n == 0 and m == 0:
            break
        order = {}
        for _ in range(m):
            i, j = list(map(int, input().split()))
            order[j] = i
        trav = set()
        task_order = []
        for i in range(1, n + 1):
            if i not in order and i not in trav:
                trav.add(i)
                task_order.append(i)
            elif i in trav:
                pass
            else:
                while True:
                    if order[i]
                    if order[i] not in order and order[i] not in trav:
                        trav.add(order[i])
                        task_order.append(order[i])
                        break
                    else:
                        print(i, order[i])
                        i = order[i]
        print(order, task_order)

