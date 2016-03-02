def count_inversion(train):
	count = 0
	for i in range(0, len(train)):
		for j in range(i+1, len(train)):
			if train[i] > train[j]:
				count = count + 1
	return(count)
if __name__ == '__main__':
	while True:
		try:
			case_number = int(input())
			for i in range(0, case_number):
				L = int(input())
				train = list(map(int, input().split()))
				print("Optimal train swapping takes",count_inversion(train),"swaps.")
		except(EOFError):
			break
