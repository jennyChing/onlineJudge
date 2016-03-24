import heapq
minHeap = [] # right of middle
maxHeap = [] # left of middle
while True:
    try:
        n = int(input())
        heapq.heappush(minHeap,n)
        # if not balanced then move the heap with 2 more nodes as the other's head
        if len(minHeap) - len(maxHeap) > 1:
            heapq.heappush(maxHeap, -heapq.heappop(minHeap))
        # swap if maxHeap head > minHeap head
        if len(maxHeap) > 0 and minHeap[0] < -maxHeap[0]:
            maxHeap[0], minHeap[0] = -minHeap[0], -maxHeap[0]
            heapq.heappush(maxHeap, heapq.heappop(maxHeap))
        print (minHeap[0] if len(minHeap) > len(maxHeap) else (minHeap[0] - maxHeap[0]) // 2)
    except(EOFError):
        break
