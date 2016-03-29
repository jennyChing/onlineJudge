while True:
    try:
        n = list(map(int, input().split()))
        sum1 = '{0:032b}'.format(n[0])
        sum2 = '{0:032b}'.format(n[1])
        result = []
        for i in range(len(sum1)):
            if (sum1[i] == '1' and sum2[i] == '0') or (sum1[i] == '0' and sum2[i] == '1'):
                result.append(1)
            else:
                result.append(0)
        result = result[::-1]
        sum_r = 0
        for i in range(len(result)):
            sum_r = sum_r + result[i] * 2**i
        print(sum_r)
    except(EOFError):
        break
