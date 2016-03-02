def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            if n == 0:
                break
            field_A = []
            n_size = 0
            while n_size < n:
                value = list(map(int, input().split()))
                n_size = n_size + len(value)
                for i in range(0, len(value)):
                    field_A.append(value[i])
            print(field_A)
            max_so_far = 0
            if max_so_far <= 0:
                print("Losing streak.")
            else:
                print("The maximum winning streak is ",max_so_far,".",sep="")
        except(EOFError):
            break
