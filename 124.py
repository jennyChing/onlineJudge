'''
Topological Ordering

124 - Following Orders

The Input

The input consists of a sequence of constraint specifications. A specification consists of two lines: a list of variables on one line followed by a list of constraints on the next line. A constraint is given by a pair of variables, where x y indicates that x < y.

The Output

For each constraint specification, all orderings consistent with the constraints should be printed. Orderings are printed in lexicographical (alphabetical) order, one per line.
Output for different constraint specifications is separated by a blank line.
'''
import itertools

def list_perm(char):
    perms = []
    for x in itertools.permutations(char, len(char)):
        perms.append(x)
    return perms


if __name__ == '__main__':
    while True:
        try:
            char = sorted(list(map(str, input().split())))
            constrain = list(map(str, input().split()))
        except(EOFError):
            break
        cons = {}
        for i in range(0, len(constrain), 2):
            if constrain[i + 1] not in cons:
                cons[constrain[i + 1]] = [constrain[i]]
            else:
                cons[constrain[i + 1]].append(constrain[i])
        valid_order = []
        used = [False] * len(char)




