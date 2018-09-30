# def diff_one(str1, str2):
#     count = 0
#     for w1, w2 in zip(str1, str2):
#         for i, v in enumerate(w1):
#             if v != w2[i]:
#                 count += 1
#             if count > 1:
#                 break
#     return count == 1

# potentials = []
# def trans(word_list, start, stop, count, path=None):
#     global potentials
#     if not path:
#         count += 1
#         path = [start]

#     if [start] == [end]:
#         return path
    
#     results = []
#     for w in word_list:
#         if diff_one(w, start) and w not in set(path):
#             # potentials.append(w)
#             sol = trans(word_list, w, stop, count, path + w)
#             results.extend(sol)
#     return results



from collections import defaultdict, namedtuple
from heapq import heappush, heappop

class NotFound(Exception):
    pass

def word_ladder(words, start, end):
    """Return a word ladder (a list of words each of which differs from
    the last by one letter) linking start and end, using the given
    collection of words. Raise NotFound if there is no ladder.

    >>> words = 'card care cold cord core ward warm'.split()
    >>> ' '.join(word_ladder(words, 'cold', 'warm'))
    'cold cord card ward warm'

    """

    # find the neighbourhood of each word

    placeholder = object()
    matches = defaultdict(list)
    neighbours = defaultdict(list)

    for word in words:
        for i, v in enumerate(word):
            pattern = tuple(placeholder if i == j else c for j, c in enumerate(word))
            m = matches[pattern]
            m.append(word)
            neighbours[word].append(m)

    # A* algorithm: see https://en.wikipedia.org/wiki/A*_search_algorithm

    # Admissible estimate of the steps to get from word to end.
    def h_score(word):
        return sum(a != b for a, b in zip(word, end))

    # Closed set: of words visited in the search.
    closed_set = set()

    # Open set: search nodes that have been found but not yet
    # processed. Accompanied by a min-heap of 4-tuples (f-score,
    # g-score, word, previous-node) so that we can efficiently find
    # the node with the smallest f-score.

    Node = namedtuple('Node', 'f g word previous')
    open_set = set([start])
    open_heap= [Node(h_score(start), 0, start, None)]
    while open_heap:
        node = heappop(open_heap)
        if node.word == end:
            result = []
            while node:
                result.append(node.word)
                node = node.previous
            
            return result[::-1]
        
        open_set.remove(node.word)
        closed_set.add(node.word)
        g = node.g + 1

       
        for nbh in neighbours[node.word]:
            for w in nbh:
                if w not in closed_set and w not in open_set:
                    next_node = Node(h_score(w)+g, g, w, node)
                    heappush(open_heap, next_node)
                    open_set.add(w)

    raise NotFound (" No ladder from {} to {}".format(start, end))




# from collections import defaultdict, namedtuple
# from heapq import heappush, heappop

# class NotFound(Exception):
#     pass

# def word_ladder(words, start, end):
#     """Return a word ladder (a list of words each of which differs from
#     the last by one letter) linking start and end, using the given
#     collection of words. Raise NotFound if there is no ladder.

#     >>> words = 'card care cold cord core ward warm'.split()
#     >>> ' '.join(word_ladder(words, 'cold', 'warm'))
#     'cold cord card ward warm'

#     """
#     # Find the neighbourhood of each word.
#     placeholder = object()
#     matches = defaultdict(list)
#     neighbours = defaultdict(list)
#     for word in words:
#         for i in range(len(word)):
#             pattern = tuple(placeholder if i == j else c
#                             for j, c in enumerate(word))
#             m = matches[pattern]
#             m.append(word)
#             neighbours[word].append(m)

#     # A* algorithm: see https://en.wikipedia.org/wiki/A*_search_algorithm

#     # Admissible estimate of the steps to get from word to end.
#     def h_score(word):
#         return sum(a != b for a, b in zip(word, end))

#     # Closed set: of words visited in the search.
#     closed_set = set()

#     # Open set: search nodes that have been found but not yet
#     # processed. Accompanied by a min-heap of 4-tuples (f-score,
#     # g-score, word, previous-node) so that we can efficiently find
#     # the node with the smallest f-score.
#     Node = namedtuple('Node', 'f g word previous')
#     open_set = set([start])
#     open_heap = [Node(h_score(start), 0, start, None)]
#     while open_heap:
#         node = heappop(open_heap)
#         if node.word == end:
#             result = []
#             while node:
#                 result.append(node.word)
#                 node = node.previous
#             return result[::-1]
#         open_set.remove(node.word)
#         closed_set.add(node.word)
#         g = node.g + 1
#         for neighbourhood in neighbours[node.word]:
#             for w in neighbourhood:
#                 if w not in closed_set and w not in open_set:
#                     next_node = Node(h_score(w) + g, g, w, node)
#                     heappush(open_heap, next_node)
#                     open_set.add(w)

#     raise NotFound("No ladder from {} to {}".format(start, end))

    
if __name__ == "__main__":
    from timeit import timeit


    dict_ = [w.strip() for w in open('dictionary.txt') if w.lower()]
    # print (len(dict_))
    five_let_words = [w for w in dict_ if len(w) == 5]
    # print (len(five_let_words))

    # print ('above' in five_let_words)
    # print ('below' in five_let_words)
    timeit(lambda:print (' '.join(word_ladder(five_let_words, 'babes', 'child'))), number = 1)

    # dears fears