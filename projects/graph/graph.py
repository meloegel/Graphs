"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        # Add a vertex to the graph.
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        # Add a directed edge to the graph.
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        # Get all neighbors (edges) of a vertex.
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        # Print each vertex in breadth-first order beginning from starting_vertex.
        q = Queue()
        visited = set()
        q.enqueue(starting_vertex)

        while q.size() > 0:
            currVertex = q.dequeue()
            if currVertex not in visited:
                visited.add(currVertex)
                print(f"{currVertex}")

                neighbors = self.get_neighbors(currVertex)
                for neighbor in neighbors:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        # Print each vertex in depth-first order beginning from starting_vertex.
        s = Stack()
        visited = set()
        s.push(starting_vertex)
        
        while s.size() > 0:
            currVertex = s.pop()
            if currVertex not in visited:
                visited.add(currVertex)
                print(f"{currVertex}")
                
                neighbors = self.get_neighbors(currVertex)
                for neighbor in neighbors:
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        # Print each vertex in depth-first order beginning from starting_vertex. This should be done using recursion.
        visited = set()

        def dft(vertex):
            if vertex in visited:
                return
            else:
                visited.add(vertex)
                print(f"{vertex}")

            neighbors = self.get_neighbors(vertex)
            for neighbor in neighbors:
                dft(neighbor)

        dft(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        # Return a list containing the shortest path from starting_vertex to destination_vertex in breath-first order.
        q = Queue()
        q.enqueue([starting_vertex])

        while q.size() > 0:
            path = q.dequeue()
            node = path[-1]
            if node == destination_vertex:
                return path
            for adj in self.get_neighbors(node):
                newPath = list(path)
                newPath.append(adj)
                q.enqueue(newPath)

    def dfs(self, starting_vertex, destination_vertex):
        # Return a list containing a path from starting_vertex to destination_vertex in depth-first order.
        s = Stack()
        s.push([starting_vertex])
        visited = set()

        while s.size() > 0:
            v = s.pop()
            lastVertex = v[-1]
            if lastVertex in visited:
                continue
            else:
                visited.add(lastVertex)
            for neighbor in self.get_neighbors(lastVertex):
                nextPath = v[:]
                nextPath.append(neighbor)

                if neighbor == destination_vertex:
                    return nextPath
                else:
                    s.push(nextPath)
                

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        # Return a list containing a path from starting_vertex to destination_vertex in depth-first order. This should be done using recursion.
   
        visited = set()

        def dfs(path):
            lastPath = path[-1]
            if lastPath in visited:
                return None
            else:
                visited.add(lastPath)
            if lastPath == destination_vertex:
                return path
            for neighbor in self.get_neighbors(lastPath):
                nextPath = path[:]
                nextPath.append(neighbor)
                found = dfs(nextPath)
                if found:
                    return found

        return dfs([starting_vertex])

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
