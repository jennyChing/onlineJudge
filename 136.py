N = {1:1}
p2 = 1
p3 = 1
p5 = 1
if __name__ == '__main__':
	for i in range(2, 1500):
		while N[p2]*2 <= N[i-1]:
			p2 = p2+1
		while N[p3]*3 <= N[i-1]:
			p3 = p3+1
		while N[p5]*5 <= N[i-1]:
			p5 = p5+1
		N[i] = min(N[p3]*3, min(N[p2]*2,N[p5]*5))
	print("The 1500\'th ugly number is ",859963392,".",sep="")
