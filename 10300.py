while True:
	try:
		testcase = int(input())
		for i in range(0, testcase):
			farmer = int(input())
			ans = 0
			for j in range(0, farmer):
				score = list(map(int, input().split()))
				sum = score[0]*score[2]
				ans = ans + sum
			print(ans)
	except(EOFError):
		break
