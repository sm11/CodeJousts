def TreeList(root):
    return [root, [], []]

def insertLeft(root, value):
    temp = root.pop(1)
    if len(temp)>1:
        root.insert(1, [value, temp, []])
    else:
        root.insert(1, [value, [], []])
    

def insertRight(root, value):
    temp = root.pop(2)
    if len(temp) > 1:
        print("len", len(temp))
        root.insert(2, [value, [], temp])
    else:
        root.insert(2, [value, [], []])

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

if __name__ == "__main__":
    pass
    r = TreeList(3)
    insertLeft(r,4)
    insertLeft(r,5)
    insertRight(r,6)
    insertRight(r,7)
    l = getLeftChild(r)
    print(l)
    print(r)

    setRootVal(l,9)
    print(r)
    insertLeft(l,11)
    print(r)
    print(getRightChild(getRightChild(r)))