while True:
    try:
        N = int(input())
        N_size = 0
        field_A = []
        field_B = [ [ 0 for i in range(N) ] for j in range(N) ]
        field_C = [ [ 0 for i in range(N) ] for j in range(N) ]
        for i in range(0,N*N):
            value = list(map(int, input().split()))
            N_size = N_size+len(value)
            for j in range(0,len(value)):
                field_A.append(value[j])
    except(EOFError):
        break
