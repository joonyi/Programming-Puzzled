import queue as Q
q = Q.PriorityQueue()
q.put(10)
q.put(1)
q.put(5)
while not q.empty():
	print(q.get())

import heapq
li = [5,7,9,1,3]
heapq.heapify(li)
heapq.heappush(li,4)
print(heapq.heappop(li))