class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class clist:
    def __init__(self,value):
        self.head = None
        self.tail = None
        self.length = 0

    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            self.length +=1
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
            self.length +=1

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length +=1
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
            self.length +=1

    def sum(self):
        temp_node = self.head
        sum = 0
        while temp_node is not None:
            sum += temp_node.value
            temp_node = temp_node.next
            if temp_node == self.head:
                break
        print(sum)

    def pop(self,value):
        temp_node = self.head
        if value == self.head.value:
            self.head = temp_node.next
            self.tail.next = self.head
        else:
            while temp_node.next.value != value:
                temp_node = temp_node.next
            if(temp_node.next == self.tail):
                self.tail = temp_node
            temp_node.next = temp_node.next.next
    
    def search(self,value):
        temp_node = self.head
        while temp_node.value is not None:
            if temp_node.value == value:
                print("Found")
                break
            temp_node = temp_node.next
            if temp_node == self.head:
                print("Value not found")
                break
        
    def insert(self,after,value):
        if self.head is None:
            self.prepend(value)
        else:
            new_node = Node(value)
            temp_node = self.head
            while temp_node.value != after:
                temp_node=temp_node.next
            if temp_node.value == self.tail.value:
                self.append(value)
            else:
                new_node.next = temp_node.next
                temp_node.next = new_node

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

    def reverse(self):
        prev_node = self.tail
        next_node = None
        current_node = self.head
        flag = True
        while flag==True:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
            if current_node == self.head:
                break
            
        self.head, self.tail = self.tail, self.head
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += '->'
        return result
    
 
clist = clist(0)
clist.prepend(10)
clist.prepend(20)
clist.prepend(30)
clist.append(5)
clist.append(3)
clist.insert(5,4)
clist.insert(3,2)
clist.pop(2)
clist.search(3)
clist.sum()
clist.sort()
print(clist)
#clist.reverse()
print(clist)
