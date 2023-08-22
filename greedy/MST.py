from graphs.datastructures import UndirectedGraph, MinHeap
import random


def prim(input_graph: UndirectedGraph) -> UndirectedGraph:
    """Compute a minimum spanning tree thanks to Prim's algorithm.

    Args:
        input_graph (UndirectedGraph): The input graph for which a minimum spanning tree should be computed

    Returns:
        UndirectedGraph: The minimum spanning tree.
    """
    if type(input_graph) != UndirectedGraph:
        raise TypeError("Please provide an input graph of type UndirectedGraph")
    # Initializing the minimum spanning tree with a randomly chosen node
    input_graph_nodes = input_graph.get_nodes()
    number_nodes = len(input_graph_nodes)
    starting_node = input_graph_nodes[random.randint(0, number_nodes - 1)]
    nodes_in_mst = set([starting_node])
    # Initializing accessible edges
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
        # Iterating over all accessible edges to find the next node to be chosen : the one that has the current minimum distance
        for edge in accessible_edges:
            start_node = edge[0]
            adjacent_node = edge[1]
            distance = input_graph.get_distance(start_node, adjacent_node)
            if distance < min_distance:
                min_distance = distance
                starting_node_to_closest = start_node
                closest_node = adjacent_node
        # Once the closest node has been selected it can be added to the minimum spanning tree
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


def prim_heap(input_graph: UndirectedGraph) -> UndirectedGraph:
    """Compute a minimum spanning tree thanks to Prim's algorithm and leveraging the heap data structure for minimum computational overhead.

    Args:
        input_graph (UndirectedGraph): The input graph for which a minimum spanning tree should be computed

    Returns:
        UndirectedGraph: The minimum spanning tree.
    """
    if type(input_graph) != UndirectedGraph:
        raise TypeError("Please provide an input graph of type UndirectedGraph")
    # Initializing the minimum spanning tree with a randomly chosen node
    input_graph_nodes = input_graph.get_nodes()
    number_nodes = len(input_graph_nodes)
    starting_node = input_graph_nodes[random.randint(0, number_nodes - 1)]
    nodes_in_mst = set([starting_node])
    minimum_spanning_tree = UndirectedGraph(weighted=True)
    minimum_spanning_tree.add_node(starting_node)

    # Initializing accessible edges. These are stored in a heap so that the min value can be kept track of.
    accessible_edges = MinHeap()
    for adjacent_node, weight in input_graph.get_adjacent_nodes_and_weights(
        starting_node
    ):
        # The edges are always stored as tuples (starting_node, ending_node)
        accessible_edges.insert((starting_node, adjacent_node), weight)

    # While there are edges going from explored to unexplored edges there are paths that exist
    while accessible_edges.get_number_nodes() != 0:
        # Extracting the node with the shortest path stored in the heap
        edge, distance = accessible_edges.extract_min()
        # If the adjacent edge is already in the minimum spanning tree it doesn't need to be added.
        if edge[1] in nodes_in_mst:
            continue
        nodes_in_mst.add(edge[1])
        minimum_spanning_tree.add_node(edge[1])
        minimum_spanning_tree.add_edge(edge[0], edge[1], distance)
        # Updating the heap with the new distances after having explored a new node.
        for adjacent_node, weight in input_graph.get_adjacent_nodes_and_weights(
            edge[1]
        ):
            if adjacent_node not in nodes_in_mst:
                accessible_edges.insert((edge[1], adjacent_node), weight)

    return minimum_spanning_tree


def kruskal():
    """Compute a minimum spanning tree thanks to Kruskal's algorithm.

    Args:
        input_graph (UndirectedGraph): The input graph for which a minimum spanning tree should be computed

    Returns:
        UndirectedGraph: The minimum spanning tree.
    """
    pass
