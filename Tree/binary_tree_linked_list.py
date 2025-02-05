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
                    return "Value not found"
                if root.value == searchValue:
                    return root
                else:
                    if root.left is not None:
                        next_queue.append(root.left)
                    if root.right is not None:
                        next_queue.append(root.right)
                queue=next_queue
        return "Value Not Found"
#print(searchNode(bt,"Drinks"))

def insertnode(rootnode, newnode):
    if not rootnode:
        return "Its's empty"
    else:
        queue = [rootnode]
        next_queue = []
        while queue != []:
            for node in queue:
                if node.left is None:
                    node.left = newnode
                    print("Left Inserted")
                    return True
                elif node.right is None:
                    node.right = newnode
                    print("Right Inserted")
                    return True
                else:
                    if node.left is not None:
                        next_queue.append(node.left)
                    if node.right is not None:
                        next_queue.append(node.right)     
            queue = next_queue
            next_queue = []  

def deepNode(rootnode):
    if not rootnode:
        return "Its's empty"
    else:
        queue = [rootnode]
        next_queue = []
        while queue != []:
            for node in queue:
                if node.left is not None:
                    next_queue.append(node.left)
                if node.right is not None:
                    next_queue.append(node.right)
            if next_queue == []:
                return queue[-1]
            queue = next_queue
            next_queue = []  

def deleteDeepNode(rootnode, deepnode):
    if not rootnode:
        return "No root node"
    else:
        queue = [rootnode]
        next_queue = []

        while queue != []:
            for node in queue:
                if node.right == deepnode:
                    node.right = None
                elif node.left == deepnode:
                    node.left = None
                else:
                    if node.left is not None:
                        next_queue.append(node.left)
                    if node.right is not None:
                        next_queue.append(node.right)
            queue = next_queue
            next_queue = []                   

def deletenode(rootnode, delval):
    if not rootnode:
        return "Its's empty"
    else:
        deepnode = deepNode(rootnode)
        queue = [rootnode]
        next_queue = []
        while queue != []:
            for node in queue:
                if node.value == delval:
                    node.value = deepnode.value
                    deleteDeepNode(rootnode,deepnode)
                    return True
                else:
                    if node.left is not None:
                        next_queue.append(node.left)
                    if node.right is not None:
                        next_queue.append(node.right)
            queue = next_queue
            next_queue = []

def delfulltree(rootnode):
    if not rootnode:
        return "No root node"
    else:
        rootnode.value = None
        rootnode.left = None
        rootnode.right = None
        print("Deleted")

new_node = Node("Milkshake")
node2 = Node("soda")
icet = Node("icetea")
insertnode(bt,new_node)
insertnode(bt,node2)
insertnode(bt,icet)
print(levelorder(bt))
deletenode(bt,"Cold")
print(levelorder(bt))
delfulltree(bt)
print(levelorder(bt))
#print(deepNode(bt).value)

#print(searchNode(bt,"Cold").right.value)