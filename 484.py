'''
SequenceManipulation Counting Sort
484 - The Department of Redundancy Department

Write a program that will remove all duplicates from a sequence of integers and print the list of unique integers occuring in the input sequence, along with the number of occurences of each.
'''
if __name__ == '__main__':
    memo = {}
    printing = []
    while True:
        try:
            value = list(map(int, input().split()))
            for n in value:
                if n not in printing:
                    printing.append(n)
                if n not in memo:
                    memo[n] = 1
                else:
                    memo[n] += 1
        except(EOFError):
            break
    printed = set()
    for i in printing:
        if i in printed:
            pass
        else:
            printed.add(i)
            print(i, memo[i])
