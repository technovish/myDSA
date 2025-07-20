from nt import TMP_MAX


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

head = Node(15)


def insert(rootnode,value):
    if not rootnode:
        return 
    if value < rootnode.value:
        if rootnode.left is None:
            rootnode.left = Node(value)
            return
        else:
            insert(rootnode.left,value)
    if value > rootnode.value:
        if rootnode.right is None:
            rootnode.right = Node(value)
            return
        else:
            insert(rootnode.right,value)
        

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

def levelorder(rootnode) -> list:
    if not rootnode:
        return []

    queue = [rootnode]
    next_queue = []
    result = []
    level = []

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

def preorder(node):
    if node is None:
        return
    print(node.value)         # Step 1: Visit the node
    preorder(node.left)       # Step 2: Visit left subtree
    preorder(node.right)      # Step 3: Visit right subtree

def max_depth(node):
    if node is None:
        return 0
    left_depth = max_depth(node.left)
    right_depth = max_depth(node.right)
    return max(left_depth,right_depth) + 1

            


insert(head,9)
insert(head,20)
insert(head,19)
insert(head,25)


print(levelorder(head))
print(max_depth(head))