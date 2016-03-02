while True:
	try:
		case_nbr = int(input())
		for i in range(0, case_nbr):
			grade = list(map(int, input().split()))
			avg = (sum(grade)-grade[0])/grade[0]
			above_avg = 0
			for j in range(1,len(grade)):
				if grade[j] > avg:
					above_avg = above_avg+1
			print('{0:.3%}'.format(above_avg/grade[0]))
	except(EOFError):
		break
