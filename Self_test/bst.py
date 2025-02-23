#BST Insert, Search, Delete, Traverse

class Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

def insert(rootnode,value):
    if not rootnode:
        return Node(value)
    if value < rootnode.value:
        rootnode.left = insert(rootnode.left,value)
    if value > rootnode.value:
        rootnode.right = insert(rootnode.right,value)
    return rootnode

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

def get_min(rootnode):
    if not rootnode:
        return rootnode
    else:
        while rootnode.left is not None:
            rootnode = rootnode.left
        return rootnode


def delete(rootnode,value):
    #Case 1: No left child
    #case 2: No right child
    if not rootnode:
        return None
    if value < rootnode.value:
        rootnode.left = delete(rootnode.left,value)
    elif value > rootnode.value:
        rootnode.right = delete(rootnode.right,value)
    else:
        if rootnode.left is None:
            return rootnode.right
        if rootnode.right is None:
            return rootnode.left
        
        temp = get_min(rootnode.right)
        rootnode.value = temp.value
        rootnode.right = delete(rootnode.right,temp.value)
    return rootnode

    
    
    
tree = Node(500)
insert(tree,300)
insert(tree,600)
insert(tree,200)
insert(tree,400)
insert(tree,700)
insert(tree,100)
delete(tree,300)
print(levelorder(tree))