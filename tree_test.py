import unittest 


class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            #t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key
    

def buildTree():
    r = BinaryTree('a')
    r.insertRight('f')
    r.insertRight('c')
    r.getRightChild().insertLeft('e')
    r.insertLeft('b')
    r.getLeftChild().insertRight('d')
    return r

class unitTest(unittest.TestCase):
    def test(self):
        self.assertEqual(ttree.getRightChild().getRootVal(),'c')
        self.assertEqual(ttree.getLeftChild().getRightChild().getRootVal(),'d')
        self.assertEqual(ttree.getRightChild().getLeftChild().getRootVal(),'e')
        self.assertEqual(ttree.getRightChild().getRightChild().getRootVal(),'f')

if __name__ == "__main__":
    ttree = buildTree()
    test = unitTest()
    test.test()