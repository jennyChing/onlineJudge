'''
Permutations

10213 - How Many Pieces of Land ?

You are given an elliptical shaped land and you are asked to choose n arbitrary points on its boundary.  Then you connect all these points with one another with straight lines (that’s n ∗ (n−1)/2 connections for n points). What is the maximum number of pieces of land you will get by choosing the points on the boundary carefully?
'''
memo = {1:1, 2:2, 3: 4, 4:8}
if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        n = int(input())
        if n in memo:
            print(memo[n])
        else:
            ans = 1 + (n - 1) * (n) // 2 + n * (n - 1) * (n - 2) * (n - 3) // 24
            memo[n] = ans
            print(ans)

