from graphs.datastructures import Graph


def topological_sort(graph: Graph) -> list:
    """Topologically sort a graph. This topological sort uses recursive DFS.

    Args:
        graph: The graph to be topologically sorted.

    Returns:
        list: The list of nodes in topological order.
    """
    nodes_to_explore = graph.get_nodes()
    explored_nodes = set()
    ordered_nodes = []
    for node in nodes_to_explore:
        if node not in explored_nodes:
            explored_nodes, ordered_nodes = recursive_topological_dfs(
                graph, node, explored_nodes, ordered_nodes
            )
    return ordered_nodes[::-1]


def recursive_topological_dfs(
    graph: Graph, start: object, explored_nodes: list, ordered_nodes: list
) -> tuple[list, list]:
    """Helper function for the topological sort of a graph. Handles the recursive DFS part.
    Orders nodes starting from a specific start node and adds these to the preexisting ordered nodes list.

    Args:
        graph: The graph on which to order on.
        start: The starting node for the ordering sequence.
        explored_nodes: The list of already explored nodes.
        ordered_nodes: The list of ordered nodes. NB these are actually in reverse order.

    Returns:
        tuple[list, list]: The updated explored_nodes and ordered_nodes lists.
    """
    explored_nodes.add(start)
    for node in graph.get_adjacent_nodes(start):
        if node not in explored_nodes:
            explored_nodes, ordered_nodes = recursive_topological_dfs(
                graph, node, explored_nodes, ordered_nodes
            )
    ordered_nodes.append(start)
    return explored_nodes, ordered_nodes
