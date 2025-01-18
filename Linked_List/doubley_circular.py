class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next, self.head.prev = self.head, new_node
            self.head = new_node
            self.tail.next = self.head

    def append (self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

    def pop (self,value):
        temp_node = self.head
        while temp_node.value != value:
            if temp_node.next == self.head:
                print("Not found")
                return False
            temp_node = temp_node.next
        temp_node.prev.next = temp_node.next
        temp_node.next.prev = temp_node.prev
        temp_node.next = None 
        temp_node.prev = None
    
    def insert (self,after,value):
        new_node = Node(value)
        temp_node = self.head
        
        while temp_node.value != after:
            if temp_node.next == self.head:
                print("Not found")
                return False
            temp_node = temp_node.next
        new_node.next = temp_node.next
        temp_node.next = new_node
        new_node.prev = temp_node

    def sort(self):
        changed = True
        while changed:
            changed = False
            current = self.head
            while current.next != self.head:
                if current.value > current.next.value:
                    current.value, current.next.value = current.next.value, current.value
                    changed = True
                current = current.next
            
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += '<->'
        return result
    
dc = LinkedList()
dc.prepend(10)
dc.prepend(5)
dc.prepend(4)
dc.append(11)
dc.pop(10)
dc.insert(5,6)
dc.sort()
print(dc)