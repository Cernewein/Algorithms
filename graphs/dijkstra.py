from graphs.datastructures import Graph, MinHeap


def dijkstra(graph: Graph, starting_node: object) -> dict:
    """Find the single source shortest path from a starting node to all other nodes in the graph

    Args:
        graph (Graph): The graph on which to compute the shortest paths
        starting_node (object): The starting node from which to computed the shortest paths

    Returns:
        dict: A dictionary containing all the graph nodes as keys with associated distances from the starting node
    """
    if type(graph) != Graph:
        raise TypeError("Please provide an input graph of type Graph")
    if starting_node not in graph.get_nodes():
        raise TypeError("Starting node not in graph !")

    # Initialising the algorithm by setting all distances to infinity (1e7)
    # and initializing the explored nodes as well as accessible edges (edges leading from the explored nodes to the unexplored nodes)
    explored_nodes = set([starting_node])
    distances = {}
    for node in graph.get_nodes():
        distances[node] = 1e7
    distances[starting_node] = 0
    accessible_edges = [
        [starting_node, adjacent_node]
        for adjacent_node in list(graph.get_adjacent_nodes(starting_node))
    ]
    # While there are edges going from explored to unexplored edges there are paths that exist
    while len(accessible_edges) != 0:
        # Initiliazing the shortest distance and the closest node
        min_distance = 1e7
        closest_node = accessible_edges[0][1]
        # Iterating over all accessible edges to find the next node to be chosen : the one that has the current minimum path
        for edge in accessible_edges:
            start_node = edge[0]
            adjacent_node = edge[1]
            # Dijkstra score
            distance = distances[start_node] + graph.get_distance(
                start_node, adjacent_node
            )
            if distance < min_distance:
                min_distance = distance
                closest_node = adjacent_node
        explored_nodes.add(closest_node)
        distances[closest_node] = min_distance
        accessible_edges = []
        # Having explored a new node, the accessible outgoing edges have changed.
        for start_node in explored_nodes:
            for adjacent_node in graph.get_adjacent_nodes(start_node):
                if adjacent_node not in explored_nodes:
                    accessible_edges.append([start_node, adjacent_node])
    return distances


def dijkstra_heap(graph: Graph, starting_node: object) -> dict:
    """Find the single source shortest path from a starting node to all other nodes in the graph. Uses the dijkstra algorithm with a Heap datastructure for better performance.

    Args:
        graph (Graph): The graph on which to compute the shortest paths
        starting_node (object): The starting node from which to computed the shortest paths

    Returns:
        dict: A dictionary containing all the graph nodes as keys with associated distances from the starting node
    """
    if type(graph) != Graph:
        raise TypeError("Please provide an input graph of type Graph")
    if starting_node not in graph.get_nodes():
        raise TypeError("Starting node not in graph !")

    # Initialising the algorithm by creating a Heap for all accessible nodes and initializing the final distances dict.
    distances = {}
    accessible_nodes = MinHeap()
    accessible_nodes.insert(starting_node, 0)

    # While there are edges going from explored to unexplored edges there are paths that exist
    while accessible_nodes.get_number_nodes() != 0:
        # Extracting the node with the shortest path stored in the heap
        node, distance = accessible_nodes.extract_min()
        if node in distances.keys():
            continue
        distances[node] = distance
        # Updating the heap with the new distances after having explored a new node.
        for adjacent_node, weight in graph.get_adjacent_nodes_and_weights(node):
            if adjacent_node not in distances.keys():
                accessible_nodes.insert(adjacent_node, distance + weight)

    # Completing the distances dict so that unexplored (unaccessible nodes have an inifinite distance from the starting node.)
    # Runs in O(n) time so there is no performance loss.
    for node, weight in graph.get_nodes_and_weights():
        if node not in distances.keys():
            distances[node] = 1e7
    return distances
