'''
Cardinality of a Set: 一個團體總共幾個人？
10608 - Friends

There is a town with N citizens. It is known that some pairs of people are friends. According to the famous saying that “The friends of my friends are my friends, too” it follows that if A and B are friends and B and C are friends then A and C are friends, too.  Your task is to count how many people there are in the largest group of friends.

2 # no. of cases
3 2 # N is the number of town’s citizens and M is the number of pairs of people
1 2 # following M lines consists of two integers A and B  which describe that A and B are friends
2 3 --> largest group: 1, 2, 3 = 3 ppl
10 12 # N is the number of town’s citizens and M is the number of pairs of people
1 2 # following M lines consists of two integers A and B  which describe that A and B are friends
3 1
3 4
5 4
3 5
4 6
5 2
2 1
7 1
1 2
9 10
8 9 --> largest group: 1, 2, 3, 4, 5, 6, 7: 7 ppl
Solution 1:
    Open an array of N groups and check each pair to move the ppl to correct group.
    Return the group with the largest number of ppl (implement refer to: 101 - The Blocks Problem
    * Use dictionary to keep track whether the value was added before:
    if not exist: group += 1 and append the pairs
    if already exist: find out the group and combine if nessary

Solution 2:
    Use a dictionary that maps the ppl and group they belongs to: key is ppl's number and value is the group number
'''
def find_group(n):
    for i in range(len(ppl)):
        if n in ppl[i]:
            return i

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N, M = list(map(int, input().split()))
        added = set()
        group = 0
        ppl = []
        for pairs in range(M):
            p = list(map(int, input().split()))
            l, r = p[0] - 1, p[1] - 1
            print(pairs)
# both already exists in two different groups: combine the two to the group with smaller index, make sure that other items in the same group are combined as well
            if l in added and r in added:
## find which group l and r are in and move all elements in the larger index group into the smaller one (***carefull: do nothing if alreay in the same group!!!)
                if find_group(l) == find_group(r):
                    pass
                else:
                    temp = ppl[find_group(r)].copy()
                    ppl[find_group(r)].clear()
                    ppl[find_group(l)].update(temp)
                #print(l, r, added, ppl)
## one exist and the other does not: add the new one into the same group
            elif l in added and r not in added:
## find the group l is in and append r to the group
                ppl[find_group(l)].add(r)
                added.add(r)
                #print(l, r, added, ppl)
            elif l not in added and r in added:
## find the group r is in and append l to the group
                ppl[find_group(r)].add(l)
                added.add(l)
                #print(l, r, added, ppl)
# both doesn't exits: open a new group and add both into the new group
            elif l not in added and r not in added:
                lst = set()
                lst.add(l)
                lst.add(r)
                ppl.append(lst)
                added.add(l)
                added.add(r)
                group += 1
                #print(l, r, added, ppl)
        largest_g = 0
        for i in range(len(ppl)):
            largest_g = max(largest_g, len(ppl[i]))
        print(largest_g)






