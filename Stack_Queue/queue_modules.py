#Collections Module
#Queue module
#Multi processing module

#1. Collection module

from collections import deque

customqueue = deque(maxlen=3)
customqueue.append(1)
customqueue.append(2)
customqueue.append(3)
customqueue.append(4)
customqueue.popleft()
customqueue.append(5)
customqueue.pop()
customqueue.clear()
print(customqueue)

#2. Queue Module
import queue as q

customQ = q.Queue(maxsize=5)
customQ.put(100)
customQ.put(101)
customQ.put(102)
customQ.put(102)
customQ.put(102)
print(customQ.qsize())
print(customQ.full())
print(customQ.get())

#3. Multiprocessing module

from multiprocessing import Queue

multiQ = Queue(maxsize=3)
multiQ.put(4)
multiQ.put(5)
multiQ.put(6)


print(multiQ.get())
