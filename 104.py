'''
Shortest path

104 - Arbitrage

The Input

The input file consists of one or more conversion tables. You must solve the arbitrage problem for each of the tables in the input file.  Each table is preceded by an integer n on a line by itself giving the dimensions of the table. The maximum dimension is 20; the minimum dimension is 2.  The table then follows in row major order but with the diagonal elements of the table missing (these are assumed to have value 1.0). Thus the first row of the table represents the conversion rates
between country 1 and n-1 other countries, i.e., the amount of currency of country i (2 <= i <= n ) that can be purchased with one unit of the currency of country 1. Thus each table consists of n+1 lines in the input file: 1 line containing n and n lines representing the conversion table.

The Output

For each table in the input file you must determine whether a sequence of exchanges exists that results in a profit of more than 1 percent (0.01). If a sequence exists you must print the sequence of exchanges that results in a profit. If there is more than one sequence that results in a profit of more than 1 percent you must print a sequence of minimal length, i.e., one of the sequences that uses the fewest exchanges of currencies to yield a profit.

Because the IRS (United States Internal Revenue Service) notices lengthy transaction sequences, all profiting sequences must consist of n or fewer transactions where n is the dimension of the table giving conversion rates. The sequence 1 2 1 represents two conversions.

If a profiting sequence exists you must print the sequence of exchanges that results in a profit. The sequence is printed as a sequence of integers with the integer i representing the  tex2html_wrap_inline51 line of the conversion table (country i). The first integer in the sequence is the country from which the profiting sequence starts. This integer also ends the sequence.
'''
def DLS(curr, path, depth):
    if depth == 0:
        if graph[path[-1]][path[0]] * curr >= 1.01:
            path.append(path[0])
            return graph [path[-1]][path[0]] * curr
        else:
            return 0
    for i in range(n):
        if i not in path:
            curr2 = curr * graph[path[-1]][i]
            path.append(i)
            value = DLS(curr2, path, depth - 1)
            if value > 0:
                return value
            path.pop()
    return 0

if __name__ == '__main__':
    while True:
        try:
            n = int(input())
        except(EOFError):
            break
        graph = []
        for i in range(n):
            c = list(map(float, input().split()))
            c.insert(i, 1.0)
            graph.append(c)
        print(graph)
        flag = False
        maxProfit, resultPath = 0, None
        for depth in range(1, n + 1):
            for start in range(n):
                path = [start]
                value = DLS(1.0, path, depth)
                if value > maxProfit:
                    maxProfit = value
                    resultPath = [p + 1 for p in path]
                    flag = True
        if flag:
            print(resultPath, maxProfit)
        else:
            print('no solution')

