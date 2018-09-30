def dfs(graph, start):
    visited, stack = list(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in set(visited):
            visited.append(vertex)
            # stack.extend(graph[vertex] - visited)
            # stack.extend(graph[vertex])
            stack.extend(graph[vertex]).difference(visited)
    return visited

def dfs_rec(graph, start, visited=list()):
    if start not in set(visited):
        visited.append(start)
        for next_ in graph[start].difference(visited):
            dfs_rec(graph, next_, visited)
    return visited


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    # count = 0
    while stack:
        # count += 1
        (vertex, path) = stack.pop()
        print (count, path)
        for next_ in graph[vertex].difference(path):
            # print ('next', next_, path) 
            if next_ == goal:
                yield path + [next_]
                # print ('p', path)
            else:
                stack.append((next_, path + [next_]))

def dfs_paths_rec(graph, start, goal, path=None):
    if not path:
        path = [start]
    if start == goal:
        yield path
    for next_ in graph[start].difference(path):
        yield from dfs_paths_rec(graph, next_, goal, path + [next_])
         

from collections import deque
def bfs(graph, start):
    visited, queue = list(), deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(graph[vertex].difference(visited))
    return visited

def bfs_rec():
    pass

def bfs_paths(graph, start, goal):
    from collections import deque
    queue = deque([(start, [start])])
    while queue:
        vertex, path = queue.popleft()
        for next_ in graph[vertex].difference(path):
            if next_ == goal:
                yield path + [next_]
            else:
                queue.append((next_, path+[next_]))


def shortest_path(graph, start, goal):
    try:
        return (next(bfs_paths(graph, start, goal)))
    except StopIteration:
        return None

            

if __name__ == "__main__":
    graph = {'A': set(['B', 'C']), 
    'B': set(['A','D', 'E']), 
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F':set(['C', 'E'])
    }

    # print (bfs(graph, 'A'))
    obj = bfs_paths(graph, 'A', 'F')
    print (list(obj))
    # print (next(obj))
    # print (shortest_path(graph, 'A', 'F'))