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
Solution 1:  TOO SLOW!!!!
    Open an array of N groups and check each pair to move the ppl to correct group.
    Return the group with the largest number of ppl (implement refer to: 101 - The Blocks Problem

Solution 2:  the key is to open to dictionaries, ones store the ppl number as key and the group they belong to as value; while the other stores group as key and the ppl number as value (a set()). When two groups are to be merged, check the ppl in the groups to be merged in the second dictionary
    Use a dictionary that maps the ppl and group they belongs to: key is ppl's number and value is the group number
'''
if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N, M = list(map(int, input().split()))
        ppl = {}
        group_name = {}
        groups = 0
        for pairs in range(M):
            p = list(map(int, input().split()))
            l, r = p[0] - 1, p[1] - 1
# both already exists in two different groups: combine the two to the group with smaller index
            if l in ppl and r in ppl and ppl[l] != ppl[r]:
                #print(ppl, group_name)
                temp = group_name[ppl[r]].copy()
                delete = ppl[r]
                group_name[ppl[l]].update(temp)
                for key, value in ppl.items():
                    if value == delete:
                        ppl[key] = ppl[l]
                group_name[delete] = set()
# one exist and the other does not: add the new one into the same group
            elif l in ppl and r not in ppl:
                ppl[r] = ppl[l]
                group_name[ppl[l]].add(r)
            elif l not in ppl and r in ppl:
                ppl[l] = ppl[r]
                group_name[ppl[r]].add(l)
# both doesn't exits: open a new group and add both into the new group
            elif l not in ppl and r not in ppl:
                group_name[groups] = set()
                group_name[groups].add(l)
                group_name[groups].add(r)
                ppl[l] = ppl[r] = groups
                groups += 1
                #print(ppl, group_name)
# use ppl's value as keys and count every time when such value exists in ppl
        max_group = 0
        for key, value in group_name.items():
            max_group = max(max_group, len(value))
        print(max_group)








