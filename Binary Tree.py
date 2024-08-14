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

tree = node(1)
tree.left = node(2)
tree.right = node(3)
tree.left.left = node(4)
tree.left.right = node(5)

tree.printTree()