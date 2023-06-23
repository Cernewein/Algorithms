from graphs.graphs import topological_sort, Graph


def find_strongly_connected_components(graph: Graph):
    reverse_ordered_nodes = topological_sort(graph)[::-1]
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
):
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
