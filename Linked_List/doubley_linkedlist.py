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

    def get(self,index):
        if index < self.length / 2:
            temp_node = self.head
            for _ in range(index):
                temp_node = temp_node.next
        else:
            temp_node = self.tail
            for _ in range(self.length-1, index, -1):
                temp_node = temp_node.prev
        return temp_node
    
    def set(self,index,value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        else:
            print("Does not exist")
            return False

    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            new_node.prev = None
            self.head = new_node
        self.length +=1

    def append (self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            new_node.next = None
            self.tail = new_node
        self.length +=1

    def insert (self,value,after):
        new_node = Node(value)
        temp_node = self.head
        while temp_node.value != after:
            temp_node = temp_node.next
        new_node.next = temp_node.next
        new_node.next.prev = new_node
        temp_node.next = new_node
        new_node.prev = temp_node
        self.length +=1

    def pop (self,value):
        temp_node = self.head
        if value == self.head.value:
            self.head = temp_node.next
            self.head.prev = None
            temp_node.next = None
        elif value == self.tail.value:
            temp_node = self.tail
            self.tail = temp_node.prev
            self.tail.next = None
        else:
            while temp_node.value != value:
                temp_node = temp_node.next
            temp_node.prev.next = temp_node.next
            temp_node.next.prev = temp_node.prev
            temp_node.next = None
            temp_node.prev = None
        self.length -=1
        
    def sort(self):
        changed = True
        while changed:
            changed = False
            current = self.head
            while current.next:
                if current.value > current.next.value:
                    current.value, current.next.value = current.next.value, current.value
                    changed = True
                current = current.next

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '<->'
            temp_node = temp_node.next
        return result


new_list = LinkedList()
new_list.prepend(100)
new_list.prepend(99)
new_list.append(102)
new_list.insert(101,100)
new_list.pop(101)
print(new_list.get(3).value)
print(new_list.set(3,105))
new_list.append(98)
new_list.append(97)
new_list.sort()
print(new_list)
#print(new_list.head.value)
#print(new_list.tail.value)
