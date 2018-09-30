class Node:
    def __init__(self, value, is_end=False):
        self.value = value
        self.is_end = is_end
        self.children = {}

    def __repr__(self):
        return repr(self.children)

def add_to_trie(word, node):
    if word == "":
        node.is_end = True
        return
    next_char, rest_of_string = word[:1], word[1:]
    if next_char in node.children:
        return add_to_trie(rest_of_string, node.children[next_char])
    
    new_node = Node(next_char, False)
    node.children[next_char] = new_node
    add_to_trie(rest_of_string, new_node)

def setup(words, node):
    for word in words:
        add_to_trie(word, node)

# def isMember(word, node):
#     if word == "":
#         if node.is_end:
#             return True
#         return False
    
#     next_char, rest_of_string = word[:1], word[1:]
#     if next_char == ".":
#         for child in node.children.values():
#             return isMember(rest_of_string, child)
#     if next_char in node.children:
#         return isMember(rest_of_string, node.children[next_char])
#     return False

def isMember(word, node):
    curr = [node]
    nxt = []

    while (word and curr):
        print (word, curr)
        next_char, word = word[:1], word[1:]
        for node in curr:
            if next_char in node.children:
                nxt.append(node.children[next_char])
        curr = nxt
        nxt = []
 

    for lastNode in curr:
        return lastNode.is_end

if __name__ == "__main__":
    t = Node("")
    words = ['hello', 'healthy', 'howdy', 'biz']
    #words = ['hi', 'hello', 'howdy', 'ho']
    setup(words, t)
    add_to_trie('hi', t)
    print (isMember('hell', t))
    #print(t.__repr__())
    add_to_trie('handsome', t)
    #print(t.__repr__())
    #print (isMember('hill', t))
    #print (isMember('.a.ds.me.', t))


