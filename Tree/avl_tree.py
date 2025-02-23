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

#Left Left Condition or Right left condition = right rotation
def rightRotation(disbalancedNode):
    newroot = disbalancedNode.left
    disbalancedNode.left = newroot.right
    newroot.right = disbalancedNode
    disbalancedNode.height = 1 + max(getheight(disbalancedNode.left), getheight(disbalancedNode.right))
    newroot.height = 1 + max(getheight(newroot.left), getheight(newroot.right))
    return newroot

#Right right or Left right condition = left rotation
def leftRotation(disbalancedNode):
    newroot = disbalancedNode.right
    disbalancedNode.right = newroot.left
    newroot.left = disbalancedNode
    disbalancedNode.height = 1 + max(getheight(disbalancedNode.left), getheight(disbalancedNode.right))
    newroot.height = 1 + max(getheight(newroot.left), getheight(newroot.right))
    return newroot

def getheight(rootnode):
    if not rootnode:
        return 0
    else:
        return rootnode.height

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

def get_min(rootnode):
    if not rootnode:
        return rootnode
    else:
        while rootnode.left is not None:
            rootnode = rootnode.left
        return rootnode

def delete(rootnode,value):
    if not rootnode:
        return rootnode
    elif value < rootnode.value:
        rootnode.left = delete(rootnode.left,value)
    elif value > rootnode.value:
        rootnode.right = delete(rootnode.right,value)
    else:
        #If root has only right child
        if rootnode.left is None:
            return rootnode.right
        #If root has only left child
        if rootnode.right is None:
            return rootnode.left
        
        temp = get_min(rootnode.right)
        rootnode.value = temp.value
        rootnode.right = delete(rootnode.right, temp.value)

    rootnode.height = 1 + max(getheight(rootnode.left), getheight(rootnode.right))
    balance = get_balance(rootnode)
    if balance > 1 and get_balance(rootnode.left) > 0:
             return rightRotation(rootnode)
    if balance < -1 and get_balance(rootnode.right) <= 0:
        return leftRotation(rootnode)
    if balance > 1 and get_balance(rootnode.left) < 0:
        rootnode.left = leftRotation(rootnode.left)
        return rightRotation(rootnode)
    if balance < -1 and get_balance(rootnode.right) > 0:
        rootnode.right = rootnode(rootnode.right)
        return leftRotation(rootnode)
    return rootnode



    

    



avl = Node(70)

insert(avl,50)
insert(avl,90)
insert(avl,30)
insert(avl,60)
insert(avl,80)
insert(avl,100)
insert(avl,20)
insert(avl,40)
insert(avl,10)
delete(avl,30)
delete(avl,80)
delete(avl,100)
print(levelorder(avl))

#print(get_balance(avl))
print(avl.right.height)
#print(get_balance(avl))