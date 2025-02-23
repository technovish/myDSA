#Children of node i is stored at (2i+1) and (2i+2)
import math
class MinHeap:
    def __init__(self):
        self.heap = []
        self.last_index = 0

    def insert(self,value):
        self.heap.append(value)
        self.last_index +=1
        self.heap.sort(reverse=True)

    #returns parents index
    def get_parent(self,value) -> int:
        index = self.heap.index(value)
        index = math.floor((index-1)/2)
        return self.heap[index]


    





bh = MinHeap()
bh.insert(100)
bh.insert(90)
bh.insert(80)
bh.insert(70)
bh.insert(60)
bh.insert(50)
bh.insert(110)
print(bh.heap)
print(bh.get_parent(100))