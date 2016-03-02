def clojureL(n, memo):
	if n in memo:
		return memo[n]
	if n&1!=0:
		l = clojureL(n>>1, memo)
	else:
		l = clojureL(3*n+1, memo)
	memo[n] = l+1
	return memo[n]

if __name__=='__main__':
	memo = {1:1}
	while True:
		try:
			n = list(map(int, input().split()))
			i = n[0]
			j = n[1]
			if i>j:
				i,j = j,i
			max_cycle = 0
			for k in range(i,j+1):
				if max_cycle < clojureL(k, memo):
					max_cycle = clojureL(k, memo)
			print(i,j,max_cycle)
		except(EOFError):
			break
