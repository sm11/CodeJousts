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
        return 
    queue = collections.deque([root])
    curr_count = 1
    next_level = 0
    level = [root.value, '\n']
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
            level.append(vertex.left.value)
            order_val.append(vertex.left.value)
        if vertex.right:
            next_level += 1
            queue.append(vertex.right)
            level.append(vertex.right.value)
            order_val.append(vertex.right.value)
        
    
        if not curr_count:
            # print ()
            curr_count, next_level = next_level, curr_count
            level.append('\n')
            if order_val:
                dic_levels[order] = order_val
                order_val = []
                order += 1

    for l in level:
        print (l, end = '' if l=='\n' else ' ')
    return dic_levels

        
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # print ("pre:\t", dfs_pre(root))
    # print ("in:\t", dfs_in(root))
    # print ("post:\t", dfs_post(root))

    root1 = Node(27)
    root1.insert(14)
    root1.insert(35)
    root1.insert(10)
    root1.insert(19)
    root1.insert(31)
    root1.insert(42)


    new_dict = print_level(root1)
    print (new_dict)


