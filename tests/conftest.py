import pytest
from graphs.datastructures import Graph


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
def reverse_test_graph():
    graph = Graph()

    graph.add_node("v")
    graph.add_node("w")
    graph.add_node("s")
    graph.add_node("t")

    graph.add_edge("t", "v")
    graph.add_edge("v", "s")
    graph.add_edge("w", "s")
    graph.add_edge("t", "w")
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
