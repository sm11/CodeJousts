# Map() Create a new, empty map.
# put(key,val) Add a new key-value pair to the map. If the key is already in the map then replace the old value with the new value.
# get(key) Given a key, return the value stored in the map or None otherwise.
# del Delete the key-value pair from the map using a statement of the form del map[key].
# len() Return the number of key-value pairs stored in the map.
# in Return True for a statement of the form key in map, if the given key is in the map.



class TreeNode:
    def __init__(self, key, val, left=None, right = None, parent=None):
        self.key = key
        self.payload = val
        self.parent = parent
        self.left_child = left
        self.right_child = right

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child():
        return self.parent and self.parent.left_child == self
    
    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not (self.parent)

    def is_leaf(self):
        return not (self.left_child and self.right_child)

    def has_any_children(self):
        # return not self.is_leaf()
        return self.left_child or self.right_child

    def replace_node_data(self, key, value, left, right):
        self.key = key
        self.payload = value
        self.left_child = left
        self.right_child = right
        if self.has_left_child():
            self.left_child .parent = self
        if self.has_right_child():
            self.right_child.parent = self

    def __iter__(self):
        if self:
            if self.has_left_child():
                for elem in self.left_child:
                    yield elem #recursive call to __iter__. same as elem.__iter__()
            yield self
            if self.has_right_child():
                for eem in self.right_child:
                    yield elem

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def length(self):
        return self.size

    def __len__(self):
        return self.size
    
    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, curr_node):
        if key < curr_node.key:
            if curr_node.has_left_child():
               self._put(key, val, curr_node.left_child)
            else:
                curr_node.left_child = TreeNode(key, val, parent=curr_node)
        else:
            if curr_node.has_right_child():
                self._put(key, val, curr_node.right_child)
            else:
                curr_node.right_child = TreeNode(key, val, parent=curr_node)
    
    def __setitem__(self, key, val):
        self.put(key,val)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
        return None
        
    def _get(self, key, curr_node):
        if not curr_node:
            return None
        if key == curr_node:
            return curr_node
        if key < curr_node:
            if curr_node.has_left_child():
                return self._get(key, curr_node.left_child)
        if key > curr_node:
            if curr_node.has_right_child():
                return self._get(key, curr_node.right_child)
        return None

    def __getitem__(self, key):
        self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        return False

    def delete(self, key):
        if self.size > 1:
            node_to_del = self._get(key, self.root)
            if node_to_del:
                self.remove(node_to_del)
                self.size -= 1
        elif self.size == 1 and self.key == key:
            self.root = None
            self.payload = None
            self.size -= 1
        else:
            raise KeyError ('Error, key not in the tree')

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, node):
        if node.is_leaf():
            if node == node.parent.left_child:
                node.parent.left_child = None
            else:
                node.parent.right_child = None

        else: # Node has at least one child
            if node.has_left_child():
                if node.is_left_child():
                    node.left_child.parent = node.parent
                    node.parent.left_child = node.left_child
                elif node.is_right_child():
                    node.left_child.parent = node.parent
                    node.parent.right_child = node.left_child
                else:
                    # Node is neither left nor right child => node is root
                    node.replace_node_data(node.left_child.key, 
                                            node.left_child.payload, 
                                            node.left_child.left, 
                                            node.left_child.right)




if __name__ == "__main__":
    pass