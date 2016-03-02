cases_nbr = 0
def swap(salary):
	for i in range(0,2):
		if salary[i] > salary[i+1]:
			salary[i],salary[i+1] = salary[i+1],salary[i]
			swap(salary)
	return(salary)
while True:
	try:
		cases = int(input())
		for i in range(0, cases):
			salary = list(map(int, input().split()))
			cases_nbr = cases_nbr + 1
			result = 0
			swap(salary)
			result = salary[1]
			print("Case ",cases_nbr,": ",result,sep="")
	except(EOFError):
		break
