while True:
	try:
		content = input()
		key=['`','1','2','3','4','5','6','7','8','9','0','-','=','Q','W','E','R','T','Y','U','I','O','P','[',']','\\','A','S','D','F','G','H','J','K','L',';','\'' , 'Z','X','C','V','B','N','M',',','.','/','\0']
#		key[' '] = ' '
		result=[0]*len(content)
		for i in range(0, len(content)):
			for j in range(0, len(key)):
				if content[i] ==" ":
					result[i]=" "
				elif content[i] == key[j]:
					result[i] = key[j-1]
		print(''.join(result))
	except(EOFError):
		break
