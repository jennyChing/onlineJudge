def inField(i,j,n,m,field):
	if i >= 0 and i < n and j >=0 and j < m and field[i][j]!="*":
		field[i][j] = int(field[i][j])+1
field_nbr = 0 
while True:
	try:
		value = list(map(int, input().split()))
		if value == [0, 0]:
			break
		n = value[0]
		m = value[1]
		field = [[0 for x in range(m)] for x in range(n)] 
		for i in range(0, n):
			row = input()
			for j in range(0, m):
				if row[j] == "*":
					field[i][j] = "*"
		for i in range(0, n):
			for j in range(0, m):
				if field[i][j] == "*":
					inField(i+1,j+1,n,m,field)
					inField(i+1,j,n,m,field)
					inField(i+1,j-1,n,m,field)
					inField(i,j+1,n,m,field)
					inField(i,j-1,n,m,field)
					inField(i-1,j+1,n,m,field)
					inField(i-1,j,n,m,field)
					inField(i-1,j-1,n,m,field)
		if field_nbr != 0:
			print()
		field_nbr = field_nbr + 1
		print("Field #",field_nbr,":",sep="")
		for i in range(0,n):
			for j in range(0,m):
				if field[i][j] == "*":
					print("*",end="")
				else:
					print(field[i][j],end="")
			print()
	except(EOFError):
		break
