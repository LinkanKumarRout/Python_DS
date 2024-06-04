# Priority Queue

# using list

pq = []

# add element
pq.append(12)
pq.append(9)
pq.append(23)
pq.append(24)
# for implimenting priority we have to sort the list in ascending or descending order
# asc - lowest the element highest the priority
# desc - highest the element highest the priority
pq.sort(reverse=False) # asc order

# removing element
pq.pop(0)
pq.pop(0)
pq.pop(0)
pq.pop(0)

# this is not best for using priority queue

# using modules

import queue

pq = queue.PriorityQueue()

# add element put() or put_nowait()
pq.put_nowait(10)
pq.put_nowait(20)
pq.put_nowait(30)
# remove element get() or get_nowait()
pq.get_nowait()
pq.get_nowait()
pq.get_nowait()

# adding a tuple

pq = []

# add element
pq.append(('linkan', 26))
pq.append(('ram', 27))
pq.append(('king', 24))

pq.sort(reverse=True)

# removing element
pq.pop(0)
pq.pop(0)
pq.pop(0)
