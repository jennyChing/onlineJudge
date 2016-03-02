while True:
	try:
		content = list(map(int, input().split()))
		table = [0]*content[0]
		table[0] = content[0]+1
		isJolly = True
		for i in range(1, len(content)-1):
			diff = abs(content[i+1] - content[i])
			if diff >= content[0] or table[diff] != 0:
				isJolly = False
				break
			else:
				table[diff] = diff
		if isJolly == True:
			print("Jolly")
		else:
			print("Not jolly")
	except(EOFError):
	  break
