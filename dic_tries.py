class Node:
    def __init__(self, value, is_end=False):
        self.value = value
        self.is_end = is_end
        self.children = {}



class Trie(Node):
    def __init__(self, value, is_end=False):
        self.root = Node(value, is_end)



    def add_to_trie(self, word):
        if word == "":
            self.root.is_end = True
            return
        next_char, rest_of_string = word[:1], word[1:]
        if next_char in self.root.children:
            return self.add_to_trie(rest_of_string)
            
        
        node = Node(next_char, False)
        self.root.children[next_char] = node
        self.add_to_trie(rest_of_string)

    def setup(self,words):
        for word in words:
            self.add_to_trie(word)

    def __repr__(self):
        return repr(self.root.children.keys()) 

    # def __repr__(self):
    #     for val in self.children.values():
    #         c = val
    #         print (c.children)
    #         while c.children:
    #             print (c.value)
    #             c = c.children
        #return repr(self.children)

def isMember(node, word):
    if word == "":
        if node.is_end:
            return True
        return False
    
    next_char, rest_of_string = word[:1], word[1:]
    if next_char == ".":
        for child in node.children.values():
            if isMember(child,rest_of_string):
                return True
 
    if next_char in node.children:
        return isMember(node.children[next_char],rest_of_string)
    return False

if __name__ == "__main__":
    t = Trie("")
    words = ['hello', 'healthy', 'howdy', 'biz']
    #   for word in words:
    t.setup(words)
    print(t.__repr__())