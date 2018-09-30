#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def largestValuesInTreeRows(t):
    from collections import deque
    
    if not t:
        return []
    
    curr_count = 1
    next_level = 0
    queue = deque([t])
    largest = [t.value]
    val = []

    while queue:
        vertex = queue.popleft()

        if vertex:
            curr_count -= 1
            
            if vertex.left:
                queue.append(vertex.left)
                val.append(vertex.left.value)
                next_level += 1
            if vertex.right:
                queue.append(vertex.right)
                val.append(vertex.right.value)
                next_level += 1
            if not curr_count:
                curr_count, next_level = next_level, curr_count
                if val:
                    largest.append(max(val))
                    val = []

    return largest
            
