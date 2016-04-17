def merge_sort(seq):
    if len(seq) < 2: return seq
    m = len(seq) // 2
    return merge(merge_sort(seq[:m]), merge_sort(seq[m:]))

def merge(l, r):
    global cnt
    result = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            cnt = cnt + (len(l) - i)
            j += 1
    result.extend(l[i:])
    result.extend(r[j:])
    return result

if __name__ == '__main__':
	while True:
		try:
			case_number = int(input())
			for i in range(0, case_number):
				L = int(input())
				train = list(map(int, input().split()))
				cnt = 0
				merge_sort(train)
				print("Optimal train swapping takes", cnt, "swaps.")
		except(EOFError):
			break
