while True:
	try:
		value = list(map(str, input().split()))
		if value == ['0', '0']:
			break
		left = value[0][::-1]
		right = value[1][::-1]
		count = 0
		isCarried = False
		for i in range(0,max(len(left),len(right))):
				int_left = int(left[i]) if i < len(left) else 0
				int_right = int(right[i]) if i < len(right) else 0
				if int_left+int_right+isCarried > 9:
					count = count + 1
					isCarried = True
				else:
					isCarried = False
		if count > 1:
			print(count, "carry operations.")
		elif count == 0:
			print ("No carry operation.")
		else:
			print(count, "carry operation.")
	except(EOFError):
		break
