'''
Data - Queue

12100 - Printer Queue
Hacker General has invented and implemented a simple priority system for the print job queue. Now, each job is assigned a priority between 1 and 9 (with 9 being the highest priority, and 1 being the lowest), and the printer operates as follows.

• The first job J in queue is taken from the queue.
• If there is some job in the queue with a higher priority than job J, then move J to the end of the queue without printing it.
• Otherwise, print job J (and do not put it back in the queue).

In this way, all those important muffin recipes that the Hacker General is printing get printed very quickly. Of course, those annoying term papers that others are printing may have to wait for quite some time to get printed, but that’s life.  Your problem with the new policy is that it has become quite tricky to determine when your print job will actually be completed. You decide to write a program to figure this out. The program will be given the current queue (as a list of priorities) as well as the position of your job in the queue, and must then calculate how long it will take until your job is printed, assuming that no additional jobs will be added to the queue. To simplify matters, we assume that printing a job always takes exactly one minute, and that adding and removing jobs from the queue is instantaneous.

Input
One line with a positive integer: the number of test cases (at most 100). Then for each test case:
    • One line with two integers n and m, where n is the number of jobs in the queue (1 ≤ n ≤ 100) and m is the position of your job (0 ≤ m ≤ n − 1). The first position in the queue is number 0, the second is number 1, and so on.
    • One line with n integers in the range 1 to 9, giving the priorities of the jobs in the queue. The first integer gives the priority of the first job, the second integer the priority of the second job, and so on.

Output
    For each test case, print one line with a single integer; the number of minutes until your job is completely printed, assuming that no additional print jobs will arrive.
'''
if __name__ == '__main__':
    cases = int(input())
    for n in range(cases):
        n_m = list(map(int, input().split()))
# n jobs in the queue and we want to know how many jobs are done when mth job is done
        n, m = n_m[0], n_m[1]
        jobs = list(map(int, input().split()))
        mint = 1
        isMax = True
        first_max = float('inf')
        for i in range(n):
            # algorithm to use O(n) time to process: sum of priority higher then me and same as me but index small er then me, and same as me after the first high priority after me
            if isMax == True and jobs[i] > jobs[m]:
                isMax = False
                first_max = i
            if jobs[i] > jobs[m] or (jobs[i] == jobs[m] and (i < m or i > first_max)):
                #print("i:", jobs[i], i, "m:", jobs[m], m, first_max)
                mint += 1
        print(mint)


