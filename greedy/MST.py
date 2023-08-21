from graphs.datastructures import UndirectedGraph
import random


def prim(input_graph: UndirectedGraph) -> UndirectedGraph:
    """Compute a minimum spanning tree thanks to Prim's algorithm.

    Args:
        input_graph (UndirectedGraph): The input graph for which a minimum spanning tree should be computed

    Returns:
        UndirectedGraph: The minimum spanning tree.
    """
    input_graph_nodes = input_graph.get_nodes()
    number_nodes = len(input_graph_nodes)
    starting_node = input_graph_nodes[random.randint(0, number_nodes - 1)]
    nodes_in_mst = set([starting_node])
    accessible_edges = [
        [starting_node, adjacent_node]
        for adjacent_node in list(input_graph.get_adjacent_nodes(starting_node))
    ]
    minimum_spanning_tree = UndirectedGraph(weighted=True)
    minimum_spanning_tree.add_node(starting_node)
    while len(accessible_edges) != 0:
        # Initiliazing the shortest distance and the closest node
        min_distance = 1e7
        closest_node = accessible_edges[0][1]
        # Iterating over all accessible edges to find the next node to be chosen : the one that has the current minimum path
        for edge in accessible_edges:
            start_node = edge[0]
            adjacent_node = edge[1]
            distance = input_graph.get_distance(start_node, adjacent_node)
            if distance < min_distance:
                min_distance = distance
                starting_node_to_closest = start_node
                closest_node = adjacent_node
        nodes_in_mst.add(closest_node)
        minimum_spanning_tree.add_node(closest_node)
        minimum_spanning_tree.add_edge(
            starting_node_to_closest, closest_node, min_distance
        )
        accessible_edges = []
        # Having explored a new node, the accessible outgoing edges have changed.
        for start_node in nodes_in_mst:
            for adjacent_node in input_graph.get_adjacent_nodes(start_node):
                if adjacent_node not in nodes_in_mst:
                    accessible_edges.append([start_node, adjacent_node])
    return minimum_spanning_tree


def kruskal():
    """Compute a minimum spanning tree thanks to Kruskal's algorithm.

    Args:
        input_graph (UndirectedGraph): The input graph for which a minimum spanning tree should be computed

    Returns:
        UndirectedGraph: The minimum spanning tree.
    """
    pass
