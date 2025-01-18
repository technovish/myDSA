class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.length = 0

class LinkedList:
    def __init__(self,value):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self,value):
        delete = self.head
        if delete.value == value:
            self.head = delete.next
            self.length -=1
        else:
            while delete.next.value != value:
                delete = delete.next

        if delete.next.value == value:
            delete.next = delete.next.next
            self.length -=1
        else:
            print("Delete value not found")

    
    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length +=1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length +=1

    def insert(self,after,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = None
            self.length +=1
        else:
            temp_loc = self.head
            while temp_loc and temp_loc.value != after:
                temp_loc = temp_loc.next

            if temp_loc is None:
                print("Value not found")
            else:
                new_node.next = temp_loc.next
                temp_loc.next = new_node
                self.length +=1
        
    def get(self,index):
        if index <0 or index > self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
    def set(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
        else:
            return False
    def reverse(self):
        prev_node = None
        next_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head, self.tail = self.tail, self.head
        
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '->'
            temp_node = temp_node.next
        return result
def newlist():
    new_list = LinkedList(0)
    new_list.append(10)
    new_list.append(11)
    new_list.append(12)
    new_list.append(13)
    new_list.prepend(45)
    new_list.prepend(44)
    new_list.insert(45,46)
    new_list.pop(13)
    new_list.set(3,47)
    new_list.set(4,48)
    new_list.set(5,49)
    #new_list.reverse()
    print (new_list)
def newlist2():
    new_list2 = LinkedList(0)
    new_list2.append(10)
    new_list2.append(11)
    new_list2.append(12)
    new_list2.append(13)
    new_list2.prepend(9)
    new_list2.prepend(8)
    print (new_list2)
    new_list2.reverse()
    print (new_list2)

newlist()
newlist2()
#print(f"List length is: {new_list.length}")


