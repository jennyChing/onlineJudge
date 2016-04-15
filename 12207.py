'''
Data - deque (double ended queue)
12207 - That is Your Queue

Input

Input consists of at most ten test cases. Each test case starts with a line containing P, the population of your country (1 ≤ P ≤ 1000000000), and C, the number of commands to process (1 ≤ C ≤ 1000).  The next C lines each contain a command of the form ‘N’, indicating the next citizen is to be admitted, or ‘E x’, indicating that citizen x is to be expedited to the front of the queue.  The last test case is followed by a line containing two zeros.

Output

For each test case print the serial of output. This is followed by one line of output for each ‘N’ command, indicating which citizen should be processed next. Look at the output for sample input for details.
'''
cases = 0
if __name__ == '__main__':
    while True:
        try:
            query = list(map(int, input().split()))
            if query == [0, 0]:
                break
            cases += 1
            print("Case ", cases, ":", sep = "")
            p, c = query[0], query[1]
            list1 = []
            list2 = []
            for i in range(min(p, c)):
                list1.append(i + 1)
            for _ in range(c):
                ctzn = input()
                if ctzn == 'N':
                    print(list1[0])
                    list1.append(list1.pop(0))
                else:
                    ctzn = list(ctzn.split())
                    E = int(ctzn[1])
                    loc = -1
                    for i in range(len(list1)):
                        if list1[i] == E:
                            loc = i
                    list2.append(E)
                    if loc == -1:
                        list2 = list2 + list1
                    else:
                        list2 = list2 + list1[:loc] + list1[loc + 1:]
                    list1 = list2
                    list2 = []
        except(EOFError):
            break
