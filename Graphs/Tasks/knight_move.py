from Graphs.graph import Graph


def legal_moves(x, y, desk_size):
    move_offsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                    (1, -2), (1, 2), (2, -1), (2, 1)]
    moves = []
    for move_x, move_y in move_offsets:
        if x + move_x in range(0, desk_size) and y + move_y in range(0, desk_size):
            moves.append((x + move_x, y + move_y))
    return moves


def build_graph(desk_size=8):
    graph = Graph()
    for y in range(desk_size):
        for x in range(desk_size):
            key = y * desk_size + x
            graph.add_vertex(key)

            new_positions = legal_moves(x, y, desk_size)
            for new_x, new_y in new_positions:
                new_key = new_y * desk_size + new_x
                graph.add_edge(key, new_key)
    return graph


def _knight_dfs(graph, vertex, path_length, path):
    vertex = graph.get_vertex(vertex)
    vertex.visited = True
    path.append(vertex)
    if len(path) - 1 < path_length:
        for nbr in vertex.get_neighbors_keys():
            if not graph.get_vertex(nbr).visited:
                if _knight_dfs(graph, nbr, path_length, path):
                    return True
        else:
            vertex.visited = False
            path.pop()
            return False
    else:
        return True


def knight_dfs(graph, start_vertex_key, path_length):
    graph.clear_search_data()

    start_vertex = graph.get_vertex(start_vertex_key)
    if not start_vertex:
        return False

    path = []
    _knight_dfs(graph, start_vertex_key, path_length, path)
    return path


g = build_graph(desk_size=8)
path = knight_dfs(g, 0, 63)
