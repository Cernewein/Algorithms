from graphs.datastructures import DirectedGraph
import numpy as np

def floyd_warhsall(graph: DirectedGraph)-> dict:
    """Compute all-pairs shortest paths for a directed input graph.

    Args:
        graph (DirectedGraph): The inpt graph for which to compute the shortest paths.

    Returns:
        dict: A dictionnary with keys being (node1, node2) and values representing the distance from node1 to node2
    """
    graph_nodes = graph.get_nodes()
    num_nodes = len(graph_nodes)
    # Initialize the solution array
    solution_array = [{(node1, node2):np.inf for node1 in graph_nodes for node2 in graph_nodes} for _ in range(num_nodes + 1) ]
    for node1 in graph_nodes:
        for node2 in graph_nodes:
            if node1 == node2:
                solution_array[0][(node1,node2)] = 0
            elif graph.get_distance(node1, node2) != np.inf:
                solution_array[0][(node1, node2)] = graph.get_distance(node1, node2)

    # Iterate over all problem sizes
    # The size of a problem is defined by the number of hops that are allowed to reach a node
    for problem_size in range(1, num_nodes + 1):
        for node1 in graph_nodes:
            for node2 in graph_nodes:
                shortest_path_with_hop = np.inf
                # First finding the minimum distance by adding a hop to reach the inspected node
                for hop_node in graph_nodes:
                    distance_with_hop = solution_array[problem_size - 1][(node1,hop_node)] + solution_array[problem_size - 1][(hop_node, node2)]
                    if distance_with_hop < shortest_path_with_hop:
                        shortest_path_with_hop = distance_with_hop
                # Choosing the solution for the inspected node and given problem size
                # Either adding a hop reduces the distances or we keep the previous solution
                solution_array[problem_size][(node1, node2)] = min(solution_array[problem_size - 1][(node1, node2)], shortest_path_with_hop)
    # If a negative cycle is present in the graph this results in a negative distance registered from one node to itself.
    for node in graph_nodes:
        if solution_array[problem_size][(node, node)] <0:
            return {}
    
    return solution_array[problem_size]