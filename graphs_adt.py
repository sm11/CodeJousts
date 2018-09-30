# Graph() creates a new, empty graph.
# addVertex(vert) adds an instance of Vertex to the graph.
# addEdge(fromVert, toVert) Adds a new, directed edge to the graph that connects two vertices.
# addEdge(fromVert, toVert, weight) Adds a new, weighted, directed edge to the graph that connects two vertices.
# getVertex(vertKey) finds the vertex in the graph named vertKey.
# getVertices() returns the list of all vertices in the graph.
# in returns True for a statement of the form vertex in graph, if the given vertex is in the graph, False otherwise.



class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def add_neighbour(self, nbr, weight=0):
        self.connected_to[nbr] = weight
    
    def __str__(self):
        return str(self.id) + ' conected to: '+str([x.id for x in self.connected_to])

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected_to[nbr]

    
class Graph:
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        self.num_vertices += 1

        return new_vertex
    
    def get_vertex(self, name):
        if name in self.vert_list:
            return self.vert_list[name]
        return None

    def __contains__(self, name):
        return name in self.vert_list
            
    def add_edge(self, from_, to_, cost=0):
        if from_ not in self.vert_list:
            new_from = self.add_vertex(from_)
        if to_ not in self.vert_list:
            new_to = self.add_vertex(to_)
        self.vert_list[from_].add_neighbour(self.vert_list[to_], cost)

    def get_vertices(self):
        return self.vert_list.keys()

    def __iter__(self):
        return iter(self.vert_list.values())


def build_graph(word_file):
    dic = {}
    graph = Graph()

    with open ('wordfile', 'r') as f:
        for line in f:
            word = line[:-1]
            for idx, _ in enumerate(word):
                bucket = word[:idx] + '_' + word[idx+1:]
                if bucket in dic:
                    dic[bucket].append(word)
                    else:
                        dic[bucket] = word


    # add veritces and edges for words in the same bucket
    for bucket in dic.keys():
        for word1 in dic[bucket]:
            for word2 in dic[bucket]:
                if word1 != word2:
                    graph.add_edge(word1, owrd2)
        
    return graph


    def traverse(y):
        vertex = y
        while (vertex.get_pred()):
            print (vertex.get_id())
            vertex = vertex.get_pred())
        print (vertex.get_id())

if __name__ == "__main__":
    graph = Graph()
    traverse(graph.get_vertex('word'))

    # for v in range(6):
    #     graph.add_vertex(v)

    # graph.add_edge(0,1,5)
    # graph.add_edge(0,5,2)
    # graph.add_edge(1,2,4)
    # graph.add_edge(2,3,9)
    # graph.add_edge(3,4,7)
    # graph.add_edge(3,5,3)
    # graph.add_edge(4,0,1)
    # graph.add_edge(5,4,8)
    # graph.add_edge(5,2,1)


    # for vertex in graph:
    #     for conn in vertex.get_connections():
    #         print ("({}, {})".format(vertex.get_id(), conn.get_id()))

