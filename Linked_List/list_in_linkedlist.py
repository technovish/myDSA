#Passing list in python linkedlist
class Node:
    def __init__(self,value):
        self.value=value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert(self,list):
        for i in list:
            new_node = Node(i)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
                self.length += 1
            else:
                self.tail.next = new_node
                new_node.prev = self.tail
                new_node.next = None
                self.tail = new_node
                self.length += 1
            
        
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '<->'
            temp_node = temp_node.next
        return result
    
ll = LinkedList()
lst = [10,20,30]
ll.insert(lst)
print(ll)
