#Binary search tree
#Left -> Value of node is less than parent
#Right - > value of node is greater than parent
#It performs faster than binary tree when inserting or deleting nodes
#1. Insert
#2. Search
#3. Delete
#4. Traversal

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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

def insert(rootnode,value):
    if not rootnode:
        return
    else:
        if value < rootnode.value:
            if rootnode.left is None:
                rootnode.left = Node(value)
            else:
                insert(rootnode.left,value)
        else:
            if rootnode.right is None:
                rootnode.right = Node(value)
            else:
                insert(rootnode.right,value)

def search(rootnode,serval):
    if not rootnode:
        return "Not present"
    else:
        if serval == rootnode.value:
            return "Found"
        elif serval < rootnode.value:
            if rootnode.left.value == serval:
                return "Found"
            else:
               return search(rootnode.left,serval)
        else:
            if rootnode.right.value == serval:
                return "Found"
            else:
               return search(rootnode.right,serval)

def minimum_value(rootnode):
    current = rootnode
    while(current.left is not None):
        current = current.left
    return current

def delete(rootnode,value):
    if rootnode is None:
        return rootnode
    if value < rootnode.value:
        rootnode.left = delete(rootnode.left,value)
    elif value > rootnode.value:
        rootnode.right = delete(rootnode.right,value)
    else:
        #Case1: Root node has only right child
        if rootnode.left is None:
            return rootnode.right
        #Case2: Root node has only left child
        if rootnode.right is None:
            return rootnode.left
        #Case3: Root node has no child or replace the root node with the left most of the right child
        temp = minimum_value(rootnode.right)
        rootnode.value = temp.value
        rootnode.right = delete(rootnode.right, temp.value)
    return rootnode


bst = Node(5)
insert(bst,3)
insert(bst,6)
insert(bst,2)
insert(bst,4)
insert(bst,7)
insert(bst,3.5)
insert(bst,3.25)

#bst = Node(4)
#print(search(bst,23))
delete(bst,3)
print(levelorder(bst))
