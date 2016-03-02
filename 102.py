import math
while True:
	try:
		value = list(map(int, input().split()))
		a = []
		for i in range(0,3):
			color = value[i]+value[i+3]+value[i+6]
			a.append(color-value[i])
			a.append(color-value[i+3])
			a.append(color-value[i+6])
		min = math.inf
		min_bin = ['B','C','G']
		for i in range(0,3):
			for j in range(0,3):
				# decrease calculation case from 9 to 6
				if i != j:
					for k in range(0,3):
						if k != j and k != i:
							sum = a[i]+a[j+3]+a[k+6]
							bin = ['B']*3
							bin[i]='B'
							bin[j]='G'
							bin[k]='C'
							if sum < min or (sum == min and ''.join(bin) < ''.join(min_bin)):
								min = sum
								min_bin = bin
		str_bin = ''.join(min_bin)						
		print(str_bin, min)
	except(EOFError):
		break
