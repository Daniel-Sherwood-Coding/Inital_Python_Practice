# method 1: inversion through recursion
class node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data, end= ' '),
        if self.right:
            self.right.printTree()
    def invertTree(self, root):
        if root == None:
            return
        root.left, root.right = self.invertTree(root.right),self.invertTree(root.left)
        return root

tree = node(1)
tree.left = node(2)
tree.right = node(3)
tree.left.left = node(4)
tree.left.right = node(5)
tree.printTree()
invertedTree = tree.invertTree(root= tree)
invertedTree.printTree()

# method 2: inversion through 