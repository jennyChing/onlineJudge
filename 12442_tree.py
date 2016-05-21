'''
function - counting cycle

12442 - Forwarding Emails

Input
The first line of input will contain T (≤ 20) denoting the number of cases.  Each case starts with a line containing an integer N (2 ≤ N ≤ 50000) denoting the number of Martians in the community. Each of the next N lines contains two integers: u v (1 ≤ u, v ≤ N, u ̸= v) meaning that Martian u forwards email to Martian v.

Output
For each case, print the case number and an integer m, where m is the Martian that the chieftain should send the initial email to. If there is more than one correct answer, output the smallest number.

Solution:
     Use a dictionary that maps the ppl and group they belongs to: key is ppl's number and value is the group number
     Find the group with the most ppl and return the initial ppl (return the smallest if the group is a cycle)
'''
def find_group(n):
    for i in range(len(ppl)):
        if n in ppl[i]:
            return i

if __name__ == '__main__':
    case = int(input())
    for cases in range(case):
        n = int(input())
        for i in range(n):
            l, r = list(map(int, input().split()))

