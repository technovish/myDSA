#stack linkedlist
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        cn = self.head
        while cn:
            yield cn
            cn = cn.next

    
class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False
    def add(self,value):
        new_node = Node(value)
        new_node.next = self.LinkedList.head
        self.LinkedList.head = new_node

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return "\n".join(values)
    
    def pop(self):
        if self.LinkedList.head is None:
            return "Stack is empty"
        else:
            self.LinkedList.head = self.LinkedList.head.next

    def delete(self):
        self.LinkedList.head = None



    
stk = Stack()
stk.add(1)
stk.add(2)
stk.add(3)
stk.pop()
print(stk)