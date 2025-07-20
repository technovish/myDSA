class BinaryT:
    def __init__(self, size):
        self.list = size * [None]
        self.maxsize = size
        self.lastUsedindex = 0
    
    def insert(self,value):
        if self.lastUsedindex+1 == self.maxsize:
            return "Tree is full"
        else:
            self.list[self.lastUsedindex+1] = value
            self.lastUsedindex+=1
    
    def search(self,value):
        for i in range(len(self.list)):
            if self.list[i] == value:
                print("Found")
                return True
        print("Not found")
        return False
    
    def preorder(self, index): #root node > left node > right node
        if index > self.lastUsedindex:
            return False
        print(self.list[index])
        self.preorder(index*2)
        self.preorder(index*2+1)

    def inoder(self,index): #left node > root node > right node
        if index > self.lastUsedindex:
            return False
        self.inoder(index*2)
        print(self.list[index])
        self.inoder(index*2+1)

    def postorder(self,index): #left node > right node > root node
        if index > self.lastUsedindex:
            return False
        self.postorder(index*2)
        self.postorder(index*2+1)
        print(self.list[index])
    
    def levelorder(self,index=1):
        for i in range(index, self.lastUsedindex+1):
            print (self.list[i])
    
    def delete(self,value):
        if self.lastUsedindex == 0:
            return "Tree is empty"
        else:
            for i in range(len(self.list)):
                if self.list[i] == value:
                    self.list[i] = self.list[self.lastUsedindex]
                    self.list[self.lastUsedindex] = None
                    self.lastUsedindex-=1
                    print("Deleted")
                    return True
        

treelist = BinaryT(20)
treelist.insert(50)
treelist.insert(25)
treelist.insert(60)
treelist.insert(22)
treelist.insert(26)
treelist.insert(52)
treelist.insert(70)
treelist.insert(21)
treelist.insert(23)
treelist.insert(55)
#treelist.preorder(1)
treelist.inoder(1)
#treelist.postorder(1)
#treelist.levelorder()
#print(treelist.list)