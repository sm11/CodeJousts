class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
    
    def insert_ordered(self, data):
        if self.value:
            if data < self.value:
                if self.left:
                    self.left.insert_ordered(data)
                else:
                    self.left = Node(data)
            else:
                if self.right:
                    self.right.insert_ordered(data)
                else:
                    self.right = Node(data)
        else:
            self.value = data


def dfs_pre(root, visited=list()):
    if root:
        visited.append(root.value)
        dfs_pre(root.left, visited)
        dfs_pre(root.right, visited)
        return visited

def dfs_in(root, visited=list()):
    if root:
        dfs_in(root.left, visited)
        visited.append(root.value)
        dfs_in(root.right, visited)
        return visited

def dfs_post(root, visited=list()):
    if root:
        dfs_post(root.left, visited)
        dfs_post(root.right, visited)
        visited.append(root.value)
        return visited

def level_order(root, visited=list()):
    pass



if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print ("pre:\t", dfs_pre(root))
    print ("in:\t", dfs_in(root))
    print ("post:\t", dfs_post(root))

    root1 = Node(27)
    root1.insert_ordered(14)
    root1.insert_ordered(35)
    root1.insert_ordered(10)
    root1.insert_ordered(19)
    root1.insert_ordered(31)
    root1.insert_ordered(42)


    rot = Node("")
    print ("pre:\t", dfs_pre(root1, []))
    # print ("in:\t", dfs_in(rot))
    print ("in:\t", dfs_in(root1, []))
    print ("post:\t", dfs_post(root1, []))
