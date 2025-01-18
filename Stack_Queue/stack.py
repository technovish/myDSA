#Stack using list

class Stack:
    def __init__(self):
        self.list = []
    
    def __str__(self):
        values = self.list
        values = [str(x) for x in reversed(self.list)]
        return "\n".join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def push(self,value):
        self.list.append(value)
       

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            return self.list.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            return self.list[len(self.list)-1]
        
    def delete(self):
        self.list = None


sl = Stack()
sl.push(1)
sl.push(2)
sl.push(3)
sl.push(4)
sl.pop()
sl.peek()
sl.delete()
print(sl)
