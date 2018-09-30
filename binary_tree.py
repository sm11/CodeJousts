class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.left_child = None
        self.right_child = None

    def insertLeft(self, newNode):
        if not self.left_child:
            self.left_child = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.left_child = self.left_child
            self.left_child = temp

    def insertRight(self, newNode):
        if not self.right_child:
            self.right_child = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.right_child = self.right_child
            self.right_child = temp

    # Accessors
    def getLeftChild(self):
        return self.left_child
    
    def getRightChild(self):
        return self.right_child
    
    def setRootVal(self, newValue):
        self.root = newValue

    def getRootVal(self):
        return self.root

if __name__ == "__main__":
    r = BinaryTree('a')
    print(r.getRootVal())
    print(r.getLeftChild())
    r.insertLeft('b')
    print(r.getLeftChild().getRootVal())
    print(r.getLeftChild().getRootVal())
    r.insertLeft('h')
    print(r.getLeftChild())
    print(r.getLeftChild().getRootVal())
    r.insertRight('c')
    print(r.getRightChild())
    print(r.getRightChild().getRootVal())
    r.getRightChild().setRootVal('hello')
    print(r.getRightChild().getRootVal())

# What are accessor methods and how are they used in OOP