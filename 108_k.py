def kadane(array):
    '''
    Kadane's dp algorithm: calculate each row's max subarray and return L, R, Sum
    '''
    maxL, maxR, maxSum = -1, -1, float('-inf')
    currL, currR, currSum = 0, 0, 0
    for i, a in enumerate(array):
        if currSum <0:
            currL, currR, currSum = i, i+1 , a
        else:
            currR, currSum = i + 1, currSum + a
        if maxSum < currSum or (maxSum == currSum and currR - currL > maxR - maxL):
            maxL, maxR, maxSum = currL, currR, currSum
    return maxL,maxR, maxSum
    #print(maxL,maxR, maxSum)

def calTrack(field):
    '''
    calculate the kadane by moving U and D and recording currSum, maxSum, maxL, maxR, maxU, and maxD here, then return the maxSum and maxL/R/U/D
    '''
    U = -1
    currSum, maxSum = 0, float('-inf')
    maxL, maxR, maxU, maxD = -1, -1, -1, -1
    for i in range(0,N):
        U = U+1
        D = -1
        temp = [[0]*N]*N
        for j in range(i,N):
            D = D+1
            rows = [0]*N
            if j>0:
                temp[j] = [sum(i) for i in zip(field[j],temp[j-1])]
            else:
                temp[j] = field[0]
            #for k in range(i,j+1):
                #rows = [sum(i) for i in zip(field[k],rows)]
            if i>0:
                rows = [x1-x2 for (x1,x2) in zip(temp[j],temp[i-1])]
            else:
                rows = temp[j]
            result = kadane(rows)
            currSum = result[2]
            if maxSum <= currSum:
                maxSum = currSum
                maxL, maxR, maxU, maxD = result[0], result[1], U, D
                #print (maxSum, maxL,maxR, maxU, maxD)
    return maxSum, maxL, maxR, maxU, maxD

if __name__ == '__main__':
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
        print(calTrack(field_B)[0])
      except(EOFError):
        break
