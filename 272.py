# find and replace the paired quotes with `` and '' respectively
# flip with boolean, isOdd should outlife the while statment, coz input() reads line by line 
isOdd = True

while True:
	try:
		content = input()
		for i in range(0, len(content)):
			if content[i] == '"':
					print("``" if isOdd else "''", end = '')
					isOdd = not isOdd
			else:
					print(content[i], end = '')
		print("")
	except(EOFError):
		break
