import pytest
from graphs.graphs import Graph, topological_sort, recursive_topological_dfs


@pytest.fixture
def test_graph():
    graph = Graph()

    graph.add_node("v")
    graph.add_node("w")
    graph.add_node("s")
    graph.add_node("t")

    graph.add_edge("v", "t")
    graph.add_edge("s", "v")
    graph.add_edge("s", "w")
    graph.add_edge("w", "t")
    return graph


@pytest.fixture
def test_graph_2():
    graph = Graph()

    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_node(5)
    graph.add_node(6)

    graph.add_edge(1, 3)
    graph.add_edge(3, 4)
    graph.add_edge(3, 5)
    graph.add_edge(4, 6)
    graph.add_edge(5, 6)
    graph.add_edge(5, 1)
    graph.add_edge(5, 2)
    return graph


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
