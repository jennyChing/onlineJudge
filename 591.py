set_nbr = 0
while True:
	try:
		stack_nbr = int(input())
		if stack_nbr ==0:
			break
		stacks = list(map(int, input().split()))
		stacks_sum = sum(stacks)
		height = stacks_sum/stack_nbr
		moves = 0
		for i in range(0, stack_nbr):
			if stacks[i] > height:
				moves = moves + stacks[i] - height
		set_nbr = set_nbr + 1
		print("Set #",set_nbr,sep="")
		print("The minimum number of moves is ",int(moves),".",sep='')
		print()
	except(EOFError):
		break
