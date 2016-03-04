def max_subarray(A):
    max_ending_here, max_so_far = 0, 0
    for index, value in enumerate(A):
        max_ending_here = max(value, max_ending_here + value)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
if __name__ == '__main__':
    while True:
        try:
            N = int(input())
            if N == 0:
                break
            field_A = []
            N_size = 0
            while N_size < N:
                value = list(map(int, input().split()))
                N_size = N_size + len(value)
                for i in range(0,len(value)):
                    field_A.append(value[i])
            #print(field_A)
            max_so_far = max_subarray(field_A)
            #max_so_far = 0
            if max_so_far<=0:
                print("Losing streak.")
            else:
                print("The maximum winning streak is ",max_so_far,".",sep="")
        except(EOFError):
           break
