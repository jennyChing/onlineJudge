while True:
	try:
		content = input()
		a = []
		for i in range(0, len(content)-1):
			if content[i].isalpha()==False:
				a.append(content.split())
		print(a)
		count = 0
		for i in range(0, len(a)-1):
			for j in range(0, len(a[i])):
				if a[i][j].isalpha():
					count = count+1
					break
		print(count)
	except(EOFError):
		break
