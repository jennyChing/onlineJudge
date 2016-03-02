import numpy
field_nbr = 0 
while True:
	try:
		value = list(map(int, input().split()))
		if value == [0, 0]:
			break
		n = value[0]
		m = value[1]
		field_nbr = field_nbr + 1
# create a empty matrix of nxm and read in value by row to fill in "*"s
		field = [[0 for x in range(m)] for x in range(n)] 
		for i in range(0, n):
			row = input()
			for j in range(0, m):
				if row[j] == "*":
					field[i][j] = "*"
		for i in range(0,n):
			for j in range(0,m):
				if field[i][j]!="*": 
					try:
						if field[i][j+1] =="*":
							field[i][j] = int(field[i][j])+1
						print(numpy.matrix(field))
						if field[i][j-1] =="*":
							field[i][j] = int(field[i][j])+1
						print(numpy.matrix(field))
						if field[i+1][j+1] =="*":
							field[i][j] = int(field[i][j])+1
						print(numpy.matrix(field))
						if field[i+1][j] =="*":
							field[i][j] = int(field[i][j])+1
						print(numpy.matrix(field))
						if field[i+1][j-1] =="*":
							field[i][j] = int(field[i][j])+1
						print(numpy.matrix(field))
						if field[i-1][j+1] =="*":
							field[i][j] = int(field[i][j])+1
						print(numpy.matrix(field))
						if field[i-1][j] =="*":
							field[i][j] = int(field[i][j])+1
						print(numpy.matrix(field))
						if field[i-1][j-1] =="*":
							field[i][j] = int(field[i][j])+1
						print(numpy.matrix(field))
					except(IndexError):	
						pass
					continue
		print("Field #",field_nbr,":",sep="")
		print(numpy.matrix(field))
	except(EOFError):
		break
			
