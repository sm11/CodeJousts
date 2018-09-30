class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None
    

    def insert(self, data):
        if self.value:
            if self.value > data:
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
            self.value = Node(data)

def print_level(root):
    import collections

    if not root:
        return None
    queue = collections.deque([root])
    curr_count = 1
    next_level = 0

    order = 1
    order_val = []
    dic_levels = {0:[root.value]}

   
    while queue:
        vertex = queue.popleft()
        curr_count -= 1
        
        # print (vertex.value, end = " ")
        if vertex.left:
            next_level += 1
            queue.append(vertex.left)
            order_val.append(vertex.left.value)
        if vertex.right:
            next_level += 1
            queue.append(vertex.right)
            order_val.append(vertex.right.value)
        
    
        if not curr_count:
            # print ()
            curr_count, next_level = next_level, curr_count

            if order_val:
                dic_levels[order] = order_val
                order_val = []
                order += 1

    return dic_levels

        
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)



    root1 = Node(27)
    root1.insert(14)
    root1.insert(35)
    root1.insert(10)
    root1.insert(19)
    root1.insert(31)
    root1.insert(33)
    root1.insert(67)
    root1.insert(40)
    root1.insert(16)
    root1.insert(55)
    root1.insert(32)


    new_dict = print_level(root1)
    for key, value in new_dict.items():
        if not (key % 2):
            print (value)
        else:
            print (value[::-1])
        # print (value)


