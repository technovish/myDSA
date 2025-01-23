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


