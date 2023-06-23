from graphs.graphs import topological_sort, recursive_topological_dfs


def test_recursive_topological_dfs(test_graph, test_graph_2):
    start = "v"
    explored_nodes = set()
    ordered_nodes = []
    explored_nodes, ordered_nodes = recursive_topological_dfs(
        test_graph, start, explored_nodes, ordered_nodes
    )
    assert explored_nodes == set(["v", "t"])
    assert ordered_nodes == ["t", "v"]

    start = 1
    explored_nodes = set()
    ordered_nodes = []
    explored_nodes, ordered_nodes = recursive_topological_dfs(
        test_graph_2, start, explored_nodes, ordered_nodes
    )
    assert explored_nodes == set([1, 2, 3, 4, 5, 6])
    assert ordered_nodes == [6, 4, 2, 5, 3, 1]


def test_topological_sort(test_graph, test_graph_2):
    assert topological_sort(test_graph) == ["s", "w", "v", "t"]
    assert topological_sort(test_graph_2) == [1, 3, 5, 2, 4, 6]
