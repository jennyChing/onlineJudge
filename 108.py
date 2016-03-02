def sum_f (N,i,j,field_B,field_C):
  for k in range(1,N+1):
    for l in range(1,N+1):
      if N+1 >= k and N+1 >= l:
        temp = [ [ field_B[k][l] for k in range(k) ] for l in range(l) ]
        print(temp,sum(map(sum, temp)))
        field_C[i][j] = sum(map(sum, temp))
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
      if N_size == N*N:
        break
    k = 0
    for i in range(0,N):
      for j in range(0,N):
        field_B[i][j] = field_A[k]
        k = k+1
    for i in range(1,N+1):
      for j in range(1,N+1):
        temp = [ [ field_B[i][j] for i in range(i) ] for j in range(j) ]
        field_C[i-1][j-1] = sum(map(sum, temp))
    max_rec = 0
    for i1 in range(0,N):
      for j1 in range(0,N):
        for i2 in range(i1,N):
          for j2 in range(j1,N):
            rec = field_C[i2][j2]-(0 if j1-1 < 0 else field_C[i2][j1-1])-(0 if i1-1 < 0 else field_C[i1-1][j2])+(0 if i1-1 < 0 or j1-1 < 0 else field_C[i1-1][j1-1])
            if rec > max_rec:
              max_rec = rec
    print(max_rec)
  except(EOFError):
    break
