from graphs.datastructures import DirectedGraph
import numpy as np

def bellman_ford(graph: DirectedGraph, starting_node: object) -> dict:
    """
    Compute the single-source distances based on given graph and starting node.

    Args:
        graph (DirectedGraph): The input graph for which the distances should be computed.
        starting_node (object): The starting node from which to compute all distances.

    Returns:
        dict: A dictionnary containing distances to all nodes from starting node. Is empty in case a negative cycle is detected.
    """
    graph_nodes = graph.get_nodes()
    num_nodes = len(graph_nodes)
    # Initialize the solution array
    solution_array = [{node:np.inf for node in graph_nodes} for _ in range(num_nodes + 1) ]
    solution_array[0][starting_node] = 0
    # Iterate over all problem sizes
    # The size of a problem is defined by the number of hops that are allowed to reach a node
    for problem_size in range(1, num_nodes + 1):
        stable = True # Helper variable to check if there is a negative cycle
        for node in graph_nodes:
            # Inspect all nodes in the graph
            shortest_path_with_hop = np.inf
            incoming_nodes = graph.get_incoming_nodes(node)
            # First finding the minimum distance by adding a hop to reach the inspected node
            for previous_node in incoming_nodes:
                distance_with_hop = solution_array[problem_size - 1][previous_node] + graph.get_distance(previous_node, node)
                if distance_with_hop < shortest_path_with_hop:
                    shortest_path_with_hop = distance_with_hop
            # Choosing the solution for the inspected node and given problem size
            # Either adding a hop reduces the distances or we keep the previous solution
            solution_array[problem_size][node] = min(solution_array[problem_size - 1][node], shortest_path_with_hop)
            if solution_array[problem_size][node] != solution_array[problem_size - 1][node]:
                stable = False
        # Once a stable solution was found we can return the solution
        if stable:
            return solution_array[problem_size - 1]
    # No stable solution has been found
    return {}