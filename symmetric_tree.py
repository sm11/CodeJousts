class Solution:
    def isMirror(self, root_left, root_right):
        if not root_left and not root_right:
            return True
        if bool(root_left and root_right):
            if root_left.val == root_right.val:
                return bool(self.isMirror(root_left.left, root_right.right)) and bool(self.isMirror(root_left.right, root_right.left))
        return False
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not rooot:
            return True
        return self.isMirror(root.left, root.right)



# Iterative solution to balanced tree problem

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack_vals = []
        if not root:
            return True
        if not (root.left or root.right):
            return True
        if bool(root.left) != bool(root.right):
            return False
        
        if root.left.val == root.right.val:
            stack_vals.append([root.left, root.right])
        else:
            return False

        while stack_vals:
            pairs = stack_vals.pop(-1)
            left = pairs[0]
            right = pairs[1]

            if bool(left) != bool(right):
                return False
            if not left and not right:
                continue
            if left.val == right.val:
                stack_vals.append((left.left, right.right))
                stack_vals.append((left.right, right.left))
            else:
                return False
        return True

