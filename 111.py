'''
Many problems in Computer Science involve maximizing some measure according to constraints.

Consider a history exam in which students are asked to put several historical events into chronological order. Students who order all the events correctly will receive full credit, but how should partial credit be awarded to students who incorrectly rank one or more of the historical events?

Some possibilities for partial credit include:

    1 point for each event whose rank matches its correct rank
    1 point for each event in the longest (not necessarily contiguous) sequence of events which are in the correct order relative to each other.
    For example, if four events are correctly ordered 1 2 3 4 then the order 1 3 2 4 would receive a score of 2 using the first method (events 1 and 4 are correctly ranked) and a score of 3 using the second method (event sequences 1 2 4 and 1 3 4 are both in the correct order relative to each other).

    In this problem you are asked to write a program to score such questions using the second method.

The Input

The first line of the input will consist of one integer n indicating the number of events with  2 <= n <= 20 . The second line will contain n integers, indicating the correct chronological order of n events. The remaining lines will each consist of n integers with each line representing a student's chronological ordering of the n events. All lines will contain n numbers in the range  tex2html_wrap_inline60 , with each number appearing exactly once per line, and with each number separated from other numbers on the same line by one or more spaces.

The Output

For each student ranking of events your program should print the score for that ranking. There should be one line of output for each student ranking.
'''

if __name__ == '__main__':
    n = int(input())
    seq = list(map(int, input().split()))
    memo = {}
    # store seq into a dictionary (key: seq[i]; value: index i/order of i) and compare the key value (index of each event) to calculate the relevant score
    for i in range(n):
        memo[seq[i]] = i
    while True:
        try:
            anw = list(map(int, input().split()))
            for i in range(len(anw)):
                for j in range(i, len(anw)):
                    if
        except(EOFError):
            break

