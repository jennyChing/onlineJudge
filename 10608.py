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

Solution 2:
    Use a dictionary that maps the ppl and group they belongs to: key is ppl's number and value is the group number
'''
if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N, M = list(map(int, input().split()))
        ppl = {}
        groups = 0
        for pairs in range(M):
            p = list(map(int, input().split()))
            l, r = p[0] - 1, p[1] - 1
# both already exists in two different groups: combine the two to the group with smaller index
            if l in ppl and r in ppl and ppl[l] != ppl[r]:
                min_g = min(l, r)
                ppl[l] = ppl[r] = ppl[min_g]
# one exist and the other does not: add the new one into the same group
            elif l in ppl and r not in ppl:
                ppl[r] = ppl[l]
            elif l not in ppl and r in ppl:
                ppl[l] = ppl[r]
# both doesn't exits: open a new group and add both into the new group
            elif l not in ppl and r not in ppl:
                ppl[l] = ppl[r] = groups
                groups += 1
        cnt = {}
# use ppl's value as keys and count every time when such value exists in ppl
        for i in range(groups):
            for j in range(len(ppl)):
                try:
                    if ppl[j] == i:
                        if i in cnt:
                            cnt[i] += 1
                        else:
                            cnt[i] = 1
                except(KeyError):
                    pass
        print(ppl)
        print(cnt)
        print(max(cnt.values()))








