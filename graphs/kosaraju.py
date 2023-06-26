from graphs.graphs import topological_sort, Graph


def find_strongly_connected_components(graph: Graph) -> dict:
    """Find the strongly connected components of a graph using the kosaraju algorithm with recursive DFS.

    Args:
        graph (Graph): The graph for which the components should be found

    Returns:
        dict: A dictionnary containing the nodes as keys and the strongly connected component number as value. If two nodes have the same value they are in the same SCC
    """
    reversed_graph = reverse_graph(graph)
    reverse_ordered_nodes = topological_sort(reversed_graph)
    explored_nodes = set()
    number_scc = 0
    strongly_connected_components = {}
    for node in reverse_ordered_nodes:
        if node not in explored_nodes:
            number_scc += 1
            (
                strongly_connected_components,
                explored_nodes,
            ) = strongly_connected_component_dfs(
                graph, node, number_scc, strongly_connected_components, explored_nodes
            )
    return strongly_connected_components


def strongly_connected_component_dfs(
    graph: Graph,
    start: object,
    number_scc: int,
    strongly_connected_components: dict,
    explored_nodes: set,
) -> tuple[dict, set]:
    """Helper function for the master find_strongly_connected_components function. This function implements the second pass of the kosaraju algorithm for finding nodes in the same current SCC.
    Uses recursive DFS.

    Args:
        graph (Graph): The graph for which the SCCs should be found.
        start (object): The starting node for exploring the current SCC.
        number_scc (int): The current SCC number. Is used for bookkeeping purposes.
        strongly_connected_components (dict): The strongly connected components dictionnary that is populated with the SCCs that have already been found. Is used for bookkeeping purposes.
        explored_nodes (set): The list of nodes that have already been explored either in a recursive call or in the outer loop of the master function. Is used for bookkeeping purposes.

    Returns:
        tuple[dict, set]: Returns the updated strongly_connected_components dictionnary along with the explored_nodes list.
    """

    strongly_connected_components[start] = number_scc
    explored_nodes.add(start)
    for node in graph.get_adjacent_nodes(start):
        if node not in explored_nodes:
            (
                strongly_connected_components,
                explored_nodes,
            ) = strongly_connected_component_dfs(
                graph, node, number_scc, strongly_connected_components, explored_nodes
            )

    return strongly_connected_components, explored_nodes


def reverse_graph(graph: Graph) -> Graph:
    """Reverse a directed input graph. The edges incoming edges are transformed into outgoing edges and vice-versa.

    Args:
        graph (Graph): The graph that should be reversed.

    Returns:
        Graph: A reversed version of the input graph.
    """
    reverse_graph = Graph()
    added_nodes = set()
    for starting_node in graph.get_nodes():
        if starting_node not in added_nodes:
            reverse_graph.add_node(starting_node)
            added_nodes.add(starting_node)
        for adjacent_node in graph.get_adjacent_nodes(starting_node):
            if adjacent_node not in added_nodes:
                reverse_graph.add_node(adjacent_node)
                added_nodes.add(adjacent_node)
            reverse_graph.add_edge(adjacent_node, starting_node)
    return reverse_graph
