while True:
	try:
		content = input()
		count = 0
		for i in range(0, len(content)-1):
			if (content[i].isalpha() and content[i+1].isalpha()==False):
				count = count+1
		if content[len(content)-1].isalpha()==True:
			print(count+1)
		else:
			print(count)
	except(EOFError):
		break
				
