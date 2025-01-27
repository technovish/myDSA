class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __str__(self):
        current_node = self.head
        result = ''
        while current_node is not None:
            result += str(current_node.value)
            if current_node.next is not None:
                result += '->'
            current_node = current_node.next

        return result
    
    def isEmpty(self):
        if self.head == None and self.tail == None:
            return True
        else:
            return False
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def dequeue(self):
        if self.head == None:
            print("No elements in Queue")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next


