while True:
	try:
		content = input()
		for i in range(0, len(content)):
			decode = ord(content[i])-7
			encode = chr(decode)
			print(encode, end = '')
		print("")
	except(EOFError):
		break

			
