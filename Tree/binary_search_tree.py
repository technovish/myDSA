#Binary search tree
#Left -> Value of node is less than parent
#Right - > value of node is greater than parent
#It performs faster than binary tree when inserting or deleting nodes

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


bst = Node(50)
insert(bst,25)
insert(bst,22)
insert(bst,60)
insert(bst,26)
print(search(bst,25))

print(levelorder(bst))
