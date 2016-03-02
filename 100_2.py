def clojureL(n, memo):
	if n in memo:
		return memo[n]
	if n % 2 == 0:
		l = clojureL(n / 2, memo)
	else:
		l = clojureL(3 * n + 1, memo)
	memo[n] = l + 1
	return memo[n]

if __name__ == '__main__':
	memo = {1: 1}

	while True:
		try:
			n = list(map(int, input().split()))
			i = n[0]
			j = n[1]
			if i > j:
				start = j
				end = i
			else:
				start = i
				end = j
			currMax = 0
			for k in range(start, end+1):
				if currMax < clojureL(k, memo):
					currMax = clojureL(k, memo)
			print(i, j, currMax)
		except(EOFError):
			break
