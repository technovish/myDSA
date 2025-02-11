#AVL Tree - Balance BST where diffrence is not more than 1 level

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

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

#Pre-order traversal Root > Left > Right
def preOrderTraverse(rootnode):
    if not rootnode:
        return 
    print(rootnode.value)
    preOrderTraverse(rootnode.left)
    preOrderTraverse(rootnode.right)

#In-Order traversal (Left > Root > Right)
def inOrderTraverse(rootnode):
    if not rootnode:
        return
    inOrderTraverse(rootnode.left)
    print(rootnode.value)
    inOrderTraverse(rootnode.right)

#Post order traversal Left > Right > Root
def postOrderTraverse(rootnode):
    if not rootnode:
        return 
    postOrderTraverse(rootnode.left)
    postOrderTraverse(rootnode.right)
    print(rootnode.value)

def getheight(rootnode):
    if not rootnode:
        return 0
    else:
        return rootnode.height

#Left Left Condition = right rotation
def rightRotation(disbalancedNode):
    newroot = disbalancedNode.left
    disbalancedNode.left = newroot.right
    newroot.right = disbalancedNode
    disbalancedNode.height = 1 + max(getheight(disbalancedNode.left), getheight(disbalancedNode.right))
    newroot.height = 1 + max(getheight(newroot.left), getheight(newroot.right))
    return newroot

#Left right condition = left rotation
def leftRotation(disbalancedNode):
    newroot = disbalancedNode.right
    disbalancedNode.right = newroot.left
    newroot.left = disbalancedNode
    disbalancedNode.height = 1 + max(getheight(disbalancedNode.left), getheight(disbalancedNode.right))
    newroot.height = 1 + max(getheight(newroot.left), getheight(newroot.right))
    return newroot

def get_balance(rootnode):
    if not rootnode:
        return 0
    else:
        return getheight(rootnode.left)-getheight(rootnode.right)
def insert(rootnode, value):
    #Case 1: Rotation is required if height diff is > 1
    #Case 2: Rotation not required
    if not rootnode:
        return Node(value)
    elif value < rootnode.value:
        rootnode.left = insert(rootnode.left,value)
    else:
        rootnode.right = insert(rootnode.right,value)

    rootnode.height = 1 + max(getheight(rootnode.left),getheight(rootnode.right))
    balance = get_balance(rootnode)
    if balance > 1 and value < rootnode.left.value:
       return rightRotation(rootnode)
    if balance > 1 and value > rootnode.left.value:
       rootnode.left = leftRotation(rootnode.left)
       return rightRotation(rootnode)
    if balance < -1 and value > rootnode.right.value:
        return leftRotation(rootnode)
    if balance < -1 and value < rootnode.right.value:
        rootnode.right = rightRotation(rootnode.right)
        return leftRotation(rootnode)
    return rootnode

avl = Node(100)
avl = insert(avl,90)
avl = insert(avl,85)
avl = insert(avl,80)
avl = insert(avl,70)
avl = insert(avl,69)
avl = insert(avl,68)
avl = insert(avl,98)
avl = insert(avl,99)
print(levelorder(avl))
print(getheight(avl))
print(avl.right.right.value)
#print(get_balance(avl))