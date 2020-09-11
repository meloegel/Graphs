class Stack():
    def __init__(self):
        self.stack = []
    def size(self):
        return len(self.stack)
    def push(self, val):
        self.stack.append(val)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

class Graph:
    def __init__(self):
        self.vertices = {}
    def addVerticies(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
    def addEdge(self, v1, v2):
        self.vertices[v1].add(v2)
    def getNeighbors(self, vertex):
        return self.vertices[vertex]

def makeGraph(ancestors):
    graph = Graph()
    for p, c in ancestors:
        graph.addVerticies(p)
        graph.addVerticies(c)
        graph.addEdge(c, p)
    return graph

def earliest_ancestor(ancestors, starting_node):
    graph = makeGraph(ancestors)
    s = Stack()
    visited = set()
    s.push([starting_node])
    longestPath = []

    while s.size() > 0:
        path = s.pop()
        currNode = path[-1]
        if len(path) > len(longestPath):
            longestPath = path
        if currNode not in visited:
            visited.add(currNode)
            p = graph.getNeighbors(currNode)
            for x in p:
                newPath = path +[x]
                s.push(newPath)
    if starting_node == longestPath[-1]:
        return -1
    else:
        return longestPath[-1]