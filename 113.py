import math
while True:
	try:
		n = float(input())
		p = float(input())
		k = pow(p, 1/n)
		result = int(round(k,1))
		print(result)
	except(EOFError):
		break
