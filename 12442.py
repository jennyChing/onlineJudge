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
        left = set()
        right = set()
        added = set()
        group = 0
        ppl = []
        for i in range(n):
            l, r = list(map(int, input().split()))
            left.add(l)
            right.add(r)
# Case 1: both already exists (in two different groups): combine the two to the group with smaller index, make sure that other items in the same group are combined as well
## find which group l and r are in and move all elements in the larger index group into the smaller one (***carefull: do nothing if alreay in the same group!!!)
            if l in added and r in added:
                if find_group(l) == find_group(r):
                    pass
                else:
                    temp = ppl[find_group(r)].copy()
                    ppl[find_group(r)].clear()
                    ppl[find_group(l)].update(temp)
## Case 2: one exist and the other does not: add the new one into the same group
## find the group l is in and append r to the group
            elif l in added and r not in added:
                ppl[find_group(l)].add(r)
                added.add(r)
## Case 3: find the group r is in and append l to the group
            elif l not in added and r in added:
                ppl[find_group(r)].add(l)
                added.add(l)
# Case 4: both doesn't exits: open a new group and add both into the new group
            elif l not in added and r not in added:
                lst = set()
                lst.add(l)
                lst.add(r)
                ppl.append(lst)
                added.add(l)
                added.add(r)
                group += 1
        largest_g = {}
        for i in range(len(ppl)):
            if len(largest_g) < len(ppl[i]):
                largest_g = ppl[i]
        print(largest_g, l, r, ppl)
        for u in largest_g:
            if u in left and u not in right:
                print(u)
                print("Case ", cases + 1, ': ', u, sep = "")
                isCycle = False
                break
            isCycle = True
        if isCycle == True:
            print("Case ", cases + 1, ': ', min(largest_g), sep = "")

