class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def levelOrder(rootnode):
    if not rootnode:
        return rootnode
    else:
        queue = [rootnode]
        next_queue = []
        result = []

        while queue != []:
            for root in queue:
                result.append(root.value)
                if root.right is not None:
                    next_queue.append(root.right)
                if root.left is not None:
                    next_queue.append(root.left)
            queue = next_queue
            next_queue = []
    return result







bh = Node(100)
print(levelOrder(bh))