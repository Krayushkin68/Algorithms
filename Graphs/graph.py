from DataStructures.queue import Queue


class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighbors = {}

        self.previous = None
        self.visited = False
        self.distance = 0

        self.time_in = -1
        self.time_out = -1

    def add_neighbor(self, neighbor, weight=0):
        self.neighbors[neighbor] = weight

    def __str__(self):
        return f'"{self.key}",  neighbors: {self.neighbors}'

    def __repr__(self):
        return f'<Vertex> "{self.key}"'

    def get_neighbors(self):
        return self.neighbors.keys()

    def get_neighbors_keys(self):
        keys = [el.get_key() for el in self.get_neighbors()]
        return keys

    def get_key(self):
        return self.key

    def get_weight(self, neighbor):
        return self.neighbors[neighbor]

    def clear_search_data(self):
        self.previous = None
        self.visited = False
        self.distance = 0
        self.time_in = -1
        self.time_out = -1


class Graph:
    def __init__(self):
        self.verticles = {}
        self.time = 0

    def add_vertex(self, key):
        new_vertex = Vertex(key)
        self.verticles[key] = new_vertex
        return new_vertex

    def add_edge(self, from_vertex, to_vertex, weight=0):
        from_vertex = self.add_vertex(from_vertex) if from_vertex not in self.verticles else self.verticles[from_vertex]
        to_vertex = self.add_vertex(to_vertex) if to_vertex not in self.verticles else self.verticles[to_vertex]
        from_vertex.add_neighbor(to_vertex, weight)

    def get_vertex(self, key):
        return self.verticles.get(key)

    def get_verticles(self):
        return self.verticles.keys()

    def __contains__(self, key):
        return key in self.verticles

    def __len__(self):
        return len(self.verticles)

    def __iter__(self):
        return iter(self.verticles.values())

    def clear_search_data(self):
        for vertex in self.verticles.values():
            vertex.clear_search_data()

    def bfs(self, start_vertex_key):
        self.clear_search_data()
        start_vertex = self.get_vertex(start_vertex_key)
        if not start_vertex:
            return False

        start_vertex.visited = True
        queue = Queue()
        queue.enqueue(start_vertex)
        while queue.size() > 0:
            cur_node = queue.dequeue()
            for nbr in cur_node.get_neighbors():
                if not nbr.visited:
                    nbr.visited = True
                    nbr.distance = cur_node.distance + 1
                    nbr.previous = cur_node
                    queue.enqueue(nbr)

    def traverse(self, vertex_key):
        vertex = self.get_vertex(vertex_key)
        if not vertex and vertex.distance == 0:
            return False
        else:
            ordered_list = []
            while vertex.previous:
                ordered_list.append(vertex)
                vertex = vertex.previous
            ordered_list.append(vertex)
        return ordered_list

    def dfs(self):
        self.clear_search_data()
        for vertex in self:
            if not vertex.visited:
                self.dfsvisit(vertex)

    def dfsvisit(self, vertex):
        vertex.visited = True
        self.time += 1
        vertex.time_in = self.time
        for nbr in vertex.get_neighbors():
            if not nbr.visited:
                nbr.previous = vertex
                self.dfsvisit(nbr)
        self.time += 1
        vertex.time_out = self.time


if __name__ == '__main__':
    g = Graph()
    for i in ['A', 'B', 'C', 'D', 'E', 'F']:
        g.add_vertex(i)

    g.add_edge('A', 'B')
    g.add_edge('A', 'D')
    g.add_edge('B', 'C')
    g.add_edge('B', 'D')
    g.add_edge('D', 'E')
    g.add_edge('E', 'B')
    g.add_edge('E', 'F')
    g.add_edge('F', 'C')

    g.dfs()

    for v in g:
        print(f'{v.time_in} - {v.time_out} : {v}')
