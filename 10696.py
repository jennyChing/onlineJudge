def f91(N,memo):
	if N in memo:
		return memo[N]
	if N <= 100:
		memo[N] = f91(f91((N+11),memo),memo)
	elif N >= 101:
		ans = N - 10
		memo[N] = ans
	return memo[N]
if __name__ == '__main__':
	memo = {}
	while True:
		try:
			value = int(input())
			if value == 0:
				break
			N = f91(value,memo)
			print("f91(",value,") = ", N,sep='')
		except(EOFError):
			break
