#Create Binary tree using linked list
# - Creation of tree
# - Insertion in the tree
# - Deletion in tree
# - Searching in tree
# - Traverse all nodes
# - Deletion of tree
import queue_linkedlist as queue

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

#creating root node
bt = Node("Drinks")


#Pre-order traversal (Left node first policy)

leftchild = Node("Hot")
rightchild = Node("Cold")
bt.left = leftchild
bt.right = rightchild
leftchild.left = Node("Tea")
leftchild.right = Node("Coffee")

def preOrderTraverse(rootnode):
    if not rootnode:
        return 
    print(rootnode.value)
    preOrderTraverse(rootnode.left)
    preOrderTraverse(rootnode.right)

#preOrderTraverse(bt)

#In-Order traversal (Left subtree first)

def inOrderTraverse(rootnode):
    if not rootnode:
        return
    inOrderTraverse(rootnode.left)
    print(rootnode.value)
    inOrderTraverse(rootnode.right)

# inOrderTraverse(bt)

def postOrderTraverse(rootnode):
    if not rootnode:
        return 
    postOrderTraverse(rootnode.left)
    postOrderTraverse(rootnode.right)
    print(rootnode.value)

#postOrderTraverse(bt)

def levelOrderTraverse(rootnode):
    if not rootnode:
        return 
    else:
        lst = []
        lst.append(rootnode.value)
        for i in range(len(lst)):
            if(rootnode.left is not None):
                lst.append(rootnode.left.value)
            if(rootnode.right is not None):
                lst.append(rootnode.right.value)
            print(rootnode.value)
            levelOrderTraverse(rootnode.left)
            levelOrderTraverse(rootnode.right)

''' def levelOrderTraverse(rootnode):
    if not rootnode:
        return 
    else:
        customq = queue.Queue()
        customq.enqueue(rootnode)
        while not (customq.isEmpty()):
            root = customq.dequeue()
            print(root.value.value)
            if (root.value.left is not None):
                customq.enqueue(root.value.left)
            if(root.value.right is not None):
                customq.enqueue(root.value.right)
        
        '''

def levelorder(rootnode) -> list:
    if rootnode is None:
        return []
    queue = [rootnode]
    next_queue = []
    level = []
    result = []

    while queue != []:
        for root in queue:
            level.append(root.value)
            if root.left is not None:
                next_queue.append(root.left)
            if root.right is not None:
                next_queue.append(root.right)
        result.append(level)
        level = []
        queue = next_queue
        next_queue = []
    return result
            
#print(levelorder(bt))
#levelOrderTraverse(bt)

def searchNode(rootnode, searchValue):
    if not rootnode:
        return "Tree is empty"
    else:
        queue = [rootnode]
        next_queue = []
        while queue != []:
            for root in queue:
                if not root:
                    return "Value nt found"
                if root.value == searchValue:
                    return "Found"
                else:
                    if root.left is not None:
                        next_queue.append(root.left)
                    if root.right is not None:
                        next_queue.append(root.right)
                queue=next_queue
        return "Value Not Found"
print(searchNode(bt,"Hot"))


