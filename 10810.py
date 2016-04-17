'''
SequenceManipulation - Insertion Sort
10810 - Ultra-QuickSort

In this problem, you have to analyze a particular sorting algorithm. The algorithm
processes a sequence of n distinct integers by swapping two adjacent
sequence elements until the sequence is sorted in ascending order. For the input
sequence
9 1 0 5 4 ,
Ultra-QuickSort produces the output
0 1 4 5 9 .
Your task is to determine how many swap operations Ultra-QuickSort needs
to perform in order to sort a given input sequence.
'''
def merge_sort(seq):
    if len(seq) < 2: return seq
    m = len(seq) // 2
    return merge(merge_sort(seq[:m]), merge_sort(seq[m:]))

def merge(l, r):
    global cnt
    result = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            cnt = cnt + (len(l) - i)
            j += 1
    result.extend(l[i:])
    result.extend(r[j:])
    return result

if __name__ == '__main__':
    while True:
        N = int(input())
        if N == 0:
            break
        seq = []
        for _ in range(N):
            n = int(input())
            seq.append(n)
        cnt = 0
        merge_sort(seq)
        print(cnt)
