class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
    
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:
            self.data = data

    def find_val(self, data):
        if data == self.data:
            return ("{} found in tree".format(data))
        if data < self.data:
            if self.left:
                return self.left.find_val(data)
            return ("{} not found in tree".format(data))
        else:
            if self.right:
                return self.right.find_val(data)
            return ("{} not found in tree".format(data))

if __name__ == "__main__":
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    print(root.find_val(7))
    print(root.find_val(14))