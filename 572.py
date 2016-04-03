'''
572 - Oil Deposits
The GeoSurvComp geologic survey company is responsible for detecting underground oil deposits. GeoSurvComp works with one large rectangular region of land at a time, and creates a grid that divides the land into numerous square plots. It then analyzes each plot separately, using sensing equipment to determine whether or not the plot contains oil. A plot containing oil is called a pocket. If two pockets are adjacent, then they are part of the same oil deposit. Oil deposits can be quite large and may contain numerous pockets. Your job is to determine how many different oil deposits are contained in a grid.
ALWAYS check your input, and make sure using = instead of ==
'''
# search through all @s and see if there are @s around it and turn all of them into '*'s recursively (count only when found @ in main function)
def check(i, j, n, m, f):
    if i < 0 or i >= m or j < 0 or j >= n or f[i][j] == '*':
        return
    f[i][j] = '*'
    check(i-1,j,n,m,f)
    check(i-1,j+1,n,m,f)
    check(i,j+1,n,m,f)
    check(i+1,j+1,n,m,f)
    check(i+1,j,n,m,f)
    check(i+1,j-1,n,m,f)
    check(i,j-1,n,m,f)
    check(i-1,j-1,n,m,f)

if __name__ == '__main__':
    while True:
        try:
            grid = list(map(int, input().split()))
            m, n = grid[0], grid[1]
            if m == 0 and n == 0:
                break
            f = []
            for i in range(m):
                line = list(input())
                f.append(line)
            cnt = 0
            for i in range(m):
                for j in range(n):
                    if f[i][j] == "@":
                        cnt += 1
                        check(i, j, n, m, f)
            print(cnt)
        except(EOFError):
            break
