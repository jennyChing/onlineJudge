# read input and split 
while True:
    try:
	value = list(map(int, raw_input().split()))
	if value[0] > value [1]:
	    result = value[0] - value[1]
	else:
	    result = value[1] - value[0]
	print(result)
    except (EOFError):
	break
