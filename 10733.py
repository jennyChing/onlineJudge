'''
Permutations

10733 - The Colored Cubes

All 6 sides of a cube are to be coated with paint. Each side is is coated uniformly with one color. When a selection of n different colors of paint is available, how many different cubes can you make?  Note that any two cubes are only to be called “different” if it is not possible to rotate the one into such a position that it appears with the same coloring as the other.
'''
def still (n):
    return n**6
def point (n):
    return 4 * 2 * n * n
def edge (n):
    return 6 * n**3
def plane (n):
    return 3 * 2 * n**3 + 3 * n**4

if __name__ =='__main__':
    while True:
        n = int(input())
        if n == 0:
            break
        ans = 0
        ans += still(n)
        ans += point(n)
        ans += edge(n)
        ans += plane(n)
        ans = ans // 24
        print(ans)
