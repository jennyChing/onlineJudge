'''
Permutaions - cube coloring

10601 - Cubes

You are given 12 rods of equal length. Each of them is colored in certain color. Your task is to determine in how many different ways one can construct a cube using these rods as edges. Two cubes are considered equal if one of them could be rotated and put next to the other, so that the corresponding edges of the two cubes are equally colored.
'''
if __name__ == '__main__':
    case = int(input())
    for _ in case:
        rod = list(map(int, input().split()))

