class Queue:
    def __init__(self):
        self.list = []

    def insert(self,value):
        self.list.append(value)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    def delete(self):
        self.list = []

    def deQueue(self):
        self.list.pop(0)
    
    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return "->".join(values)


q = Queue()
q.insert(1)
q.insert(2)
q.insert(3)
q.deQueue()
print(q)
