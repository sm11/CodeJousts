class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.left_child = None
        self.right_child = None

    def insertLeft(self, newNode):
        temp = BinaryTree(newNode)
        temp.left_child, self.left_child  = self.left_child, temp

    def insertRight(self, newNode):
        temp = BinaryTree(newNode)
        temp.right_child, self.right_child = self.right_child, temp

    #Accessors
    def getRootVal(self):
        return self.root
    
    def getLeftChild(self):
        return self.left_child
    
    def getRightChild(self):
        return self.right_child
    
    def setRootVal(self, newVal):
        self.root = newVal


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        return self.stack.pop(-1)

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)


class ParseTree(BinaryTree):
    def __init__(self, root):
        BinaryTree.__init__(root)

def build_tree(expr):
    # expr = ( 3 + ( 4 * 5 ) )
    # arr = ['(', '3', '+', '(', '4', '*', '5' ,')',')']

    arr = expr.split()
    parseTree = BinaryTree('')
    parseStack = Stack()
    parseStack.push(parseTree)
    currTree = parseTree

    for el in arr:
        if el == '(':
            currTree.insertLeft('')
            parseStack.push(currTree)
            currTree = currTree.getLeftChild()
        elif el not in ['+','-','/','*',')']:
            currTree.setRootVal(int(el))
            currTree = parseStack.pop()
        elif el in ['+','-','/','*']:
            currTree.setRootVal(el)
            currTree.insertRight('')
            parseStack.push(currTree)
            currTree = currTree.getRightChild()
        elif el == ')':
            currTree = parseStack.pop()
        else:
            raise ValueError
    return parseTree


if __name__ == "__main__":
    pt = build_tree("( ( 10 + 5 ) * 3 )")

        





    