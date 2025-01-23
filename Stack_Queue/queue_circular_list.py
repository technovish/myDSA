''' 
Queue with list capacity = Circular Queue
Works on FIFO 
'''
class Queue:
    def __init__(self, max):
        self.list = max * [None]
        self.max = max
        self.start = -1
        self.top = -1
    
    def __str__(self):
        values = [str(x) for x in self.list]
        return "->".join(values)
    
    def isFull(self):
        if self.top+1 == self.start:
            True
        elif self.start == 0 and self.top+1 == self.max:
            return True
        else:
            False
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
        
    def enqueue(self,value):
        if self.isFull():
            return "Queue is full"
        else:
            if self.top + 1 == self.max:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.list[self.top] = value
            return "Element is Added"

    def dequeue(self):
        if self.isEmpty():
            "Queue is empty"
        else:
            if self.start + 1 == self.max:
                self.list[self.start] = None
                self.start = 0
            else:
                self.list[self.start] = None
                self.start += 1
    

q = Queue(6)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
q.dequeue()
q.enqueue(70)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
print(q.start)
print(q.top)
print(q)