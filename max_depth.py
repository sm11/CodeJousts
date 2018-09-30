#answer = 0
def max_depth(root, depth, answer= 0):
    # if root == None
    if not root:
        return
    # if leaves are reached
    if not root.left and not root.right:
        answer =  max(answer, depth)
    max_depth(root.left, depth + 1, answer)
    max_depth(root.right, depth + 1, answer)

class Solution:
    def __init__(self):
        self.answer = 0
    def maxDepth(self, root, depth=1):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return 0
        if not root.left and not root.right:
            self.answer = max(depth, self.answer)
        self.maxDepth(root.left, depth+1)
        self.maxDepth(root.right, depth+1)
        return self.answer

def max_depth_bu(root):
    if not root:
        return 0
    left_depth = max_depth_bu(root.left)
    right_depth = max_depth_bu(root.right)
    return  max(left_depth, right_depth)+1