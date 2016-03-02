while True:
	try:
		value = int(input())
		for i in range(0,value):
			a = int(input())
			b = int(input())
			if a%2!=0 and b%2!=0: 
				sum = int((b+1)*(b+1)/4 - (a-1)*(a-1)/4)
			elif a%2!=0 and b%2==0:	
				sum = int((b)*(b)/4 - (a-1)*(a-1)/4)
			elif a%2==0 and b%2!=0:	
				sum = int((b+1)*(b+1)/4 - (a)*(a)/4)
			else:
				sum = int((b)*(b)/4 - (a)*(a)/4)
			print('Case ',i+1,': ',sum, sep='')
	except(EOFError):
		break
