from graphs.datastructures import Graph


def dijkstra(graph: Graph, starting_node: object):
    explored_nodes = set(starting_node)
    distances = {}
    for node in graph.get_nodes():
        distances[node] = 1e7
    distances[starting_node] = 0
    accessible_edges = [
        [starting_node, adjacent_node]
        for adjacent_node in list(graph.get_adjacent_nodes(starting_node))
    ]
    while len(accessible_edges) != 0:
        min_distance = 1e7
        closest_node = accessible_edges[0][1]
        for edge in accessible_edges:
            start_node = edge[0]
            adjacent_node = edge[1]
            distance = distances[start_node] + graph.get_distance(
                start_node, adjacent_node
            )
            if distance < min_distance:
                min_distance = distance
                closest_node = adjacent_node
        explored_nodes.add(closest_node)
        distances[closest_node] = min_distance
        accessible_edges = []
        for start_node in explored_nodes:
            for adjacent_node in graph.get_adjacent_nodes(start_node):
                if adjacent_node not in explored_nodes:
                    accessible_edges.append([start_node, adjacent_node])
    return distances
