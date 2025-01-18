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
    
    def remove_duplicate(self):
        temp = self.head
        while temp:
            check = temp.next
            while check:
                if check.value == temp.value:
                    self.pop(check.value)
                check = check.next
            temp = temp.next
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
                result += '->'
            temp_node = temp_node.next
        return result

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
#print (new_list)

new_list2 = LinkedList(0)
new_list2.append(10)
new_list2.append(11)
new_list2.append(12)
new_list2.append(13)
new_list2.prepend(50)
new_list2.prepend(51)
new_list2.insert(51,52)
#new_list2.pop(51)
new_list2.set(3,53)
new_list2.set(4,54)
new_list2.set(5,55)
new_list2.insert(54,53)
new_list2.remove_duplicate()
#new_list2.prepend(49)
print (new_list2)
new_list2.sort()
new_list2.reverse()
print (new_list2)
#print(new_list2.length)
#new_list2.pop(54)
#new_list2.reverse()
#print (new_list2)