
if __name__ == '__main__':
    while True:
        try:
            for i in range(2):
                s1 = list(input())
                s2 = list(input())
                table = [[0 for x in range(len(s2)+1)] for x in range(len(s1)+1)]
                com = 0
                for i in range(len(s1)):
                    for j in range(len(s2)):
                        if s1[i] == s2[j]:
                            table[i][j] = table[i-1][j-1] + 1
                        else:
                            table[i][j] = max(table[i-1][j], table[i][j-1])
                com = table[len(s1)-1][len(s2)-1]
                print(com)
        except(EOFError):
            break
