class TreeNode:
    def __init__(self, value, children = []):
        self.value = value
        self.children = children
    
    def __str__(self,level=0):
        ret = " " * level + str(self.value) + '\n'
        for child in self.children:
            ret += child.__str__(level+1)
        return ret
    
    def addChild(self,TreeNode):
        self.children.append(TreeNode)

tree = TreeNode("Drinks",[])
cold = TreeNode("Cold",[]) 
hot = TreeNode("Hot",[])
tea = TreeNode("Tea",[])
mojito = TreeNode("Mojito",[])

tree.addChild(cold)
tree.addChild(hot)
hot.addChild(tea)
cold.addChild(mojito)
print(tree)
