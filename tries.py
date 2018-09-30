class Trie:
    def __init__(self):
        self.end_ = '*'
        self.trie = dict()

    def make_trie(self, *words):
        for word in words:
            temp_dict = self.trie
            for letter in word:
                temp_dict = temp_dict.setdefault(letter, {})
            temp_dict[self.end_] = self.end_

        return self.trie

    def __repr__(self):
        return repr(self.trie)


    def find_word(self, word):
        sub_trie = self.trie
        for letter in word:
            if letter in sub_trie:
                sub_trie = sub_trie[letter]
            else:
                return False
        if self.end_ in sub_trie:
            return True
        else:
            return False

# """
#     def find_word_rec(self, word, sub = None):
#         if not sub:
#             sub_trie = self.trie
#         else:
#             sub_trie = sub
#         next_char, rest_of_string = word[:1], word[1:]
#         print (next_char)
#         if next_char == ".":
#             for child in sub_trie:
#                 return child.find_word_rec(rest_of_string, sub_trie[child])
#         if next_char in sub_trie:
#             return self.find_word_rec(rest_of_string, sub_trie[next_char])
#         else:
#             print ("Uhla")
#             return False
       
#         if self.end_ in sub_trie:
#             return True
#         else:
#             return False

#     """

    def add_word(self, word):
        if self.find_word(word):
            print ("word in dictionary")
            return self.trie

        temp_dict = self.trie
        for letter in word:
            if letter in temp_dict:
                temp_dict = temp_dict[letter]
            else:
                temp_dict = temp_dict.setdefault(letter, {})
        temp_dict[self.end_] = self.end_
        return self.trie   

# def isMember(node, word):
#     if word == "":
#         if node.key == node.end_:
#             return True
#         return False
    
#     next_char, rest_of_string = word[:1], word[1:]
#     if next_char == ".":
#         for child in node.trie.values():
#             if isMember(child,rest_of_string):
#                 return True
#     if next_char in node:
#         return isMember(node[next_char],rest_of_string)
#     return False


def isMember(word, node):
    curr = [node.trie]
    nxt = []

    while (word and curr):
        print(word, curr)
        next_char = word[:1]

        for nde in curr:
            print ("node", nde)
            if next_char in nde:
                nxt.append(nde[next_char])
            elif next_char == '.':
                nxt.append(nde.values())
            else:
                break
        if not nxt:
            print ("break")
            break

        curr = nxt
        nxt = []
        word = word[1:]

    for lastNode in curr:
        return '*' in lastNode and not word
     




if __name__ == '__main__':
    trie = Trie()
    trie.make_trie('hi', 'hello', 'howdy')
    #print (trie)
    #print (trie.find_word_rec('ho')) 
    trie.add_word("ho")
    print(trie)
    #print (trie.find_word_rec('h.')) 
    print(isMember("h...", trie))
    