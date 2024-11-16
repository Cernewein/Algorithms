from graphs.datastructures import UndirectedGraph


def nearest_neighbor_tsp(
    locations_graph: UndirectedGraph, starting_node: object
) -> UndirectedGraph:
    """
    Compute a TSP tour using a greedy approach. 
    It starts at a a given node and computes a tour by iteratively adding the closest next node to visit.
    The algorithm stops once it returned to the starting node.
    
    Args:
        locations_graph: The graph representing all distances between points
        starting_node: The node where the tour should initially start

    Returns:
        UndirectedGraph: The computed TSP tour
    """
    tsp_tour = UndirectedGraph(weighted=True)
    tsp_tour.add_node(starting_node)
    adjacent_nodes = locations_graph.get_adjacent_nodes_and_weights(starting_node)
    next_node = starting_node
    current_node = starting_node
    shortest_distance_to_neighbor = None
    for neighbors in adjacent_nodes:
        if shortest_distance_to_neighbor is None:
            next_node = neighbors[0]
            shortest_distance_to_neighbor = neighbors[1]
        elif neighbors[1] <= shortest_distance_to_neighbor:
            next_node = neighbors[0]
            shortest_distance_to_neighbor = neighbors[1]

    while tsp_tour.get_nodes() != locations_graph.get_nodes():
        tsp_tour.add_node(next_node)
        tsp_tour.add_edge(current_node, next_node, shortest_distance_to_neighbor)
        current_node = next_node
        shortest_distance_to_neighbor = None
        adjacent_nodes = locations_graph.get_adjacent_nodes_and_weights(current_node)
        for neighbors in adjacent_nodes:
            neighbor_node = neighbors[0]
            neighbor_distance = neighbors[1]
            if neighbor_node not in tsp_tour.get_nodes():
                if shortest_distance_to_neighbor is None:
                    next_node = neighbor_node
                    shortest_distance_to_neighbor = neighbor_distance
                elif neighbor_distance <= shortest_distance_to_neighbor:
                    next_node = neighbor_node
                    shortest_distance_to_neighbor = neighbor_distance

    if current_node != starting_node:
        shortest_distance_to_neighbor = locations_graph.get_distance(
            current_node, starting_node
        )
        tsp_tour.add_edge(current_node, starting_node, shortest_distance_to_neighbor)

    return tsp_tour
