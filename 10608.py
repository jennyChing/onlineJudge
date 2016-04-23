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
'''
if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N_M = list(map(int, input().split()))
        N, M = N_M[0], N_M[1]
        ppl = []
        for n in range(N):
            ppl.append[i]
        print(ppl)
        for pairs in range(M):
            p = list(map(int, input().split()))



