def reverse(n,count):
	# identify if the input n is symetric, if not then reverse and add to n and count one
	for i in range(0,len(n)):
		if n[len(n)-1-i] != n[i]:
			count = count+1
			#call iterate funtion and passing current count value
			n = reverse(str(int(n)+int(n[::-1])),count)
			return(n)
	print(count, n)
if __name__ == '__main__':
	while True:
		try:
			#first line of input tells how many test cases will there be
			case_number = int(input())
			#first for loop takes input line limited to the value of test cases
			for i in range(0,case_number):
				n = input()
				count = 0
				reverse(n, count)
		except(EOFError):
			break
