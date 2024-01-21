import pytest
from graphs.datastructures import UndirectedGraph, DirectedGraph


@pytest.fixture
def test_graph():
    graph = DirectedGraph()

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
    graph = DirectedGraph()

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
    graph = DirectedGraph()

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


@pytest.fixture
def test_graph_weighted():
    graph = UndirectedGraph(weighted=True)

    graph.add_node("s")
    graph.add_node("v")
    graph.add_node("w")
    graph.add_node("t")

    graph.add_edge("s", "v", 1)
    graph.add_edge("s", "w", 4)
    graph.add_edge("v", "w", 2)
    graph.add_edge("t", "t", 6)
    graph.add_edge("w", "t", 3)

    return graph


@pytest.fixture
def test_graph_weighted_2():
    graph = UndirectedGraph(weighted=True)

    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_node(5)

    graph.add_edge(1, 2, 2)
    graph.add_edge(2, 4, 3)
    graph.add_edge(2, 3, 6)
    graph.add_edge(4, 3, 2)
    graph.add_edge(3, 5, 4)

    return graph

@pytest.fixture
def test_directed_graph_weighted():
    graph = DirectedGraph(weighted=True)

    graph.add_node("s")
    graph.add_node("v")
    graph.add_node("w")
    graph.add_node("t")

    graph.add_edge("s", "v", 1)
    graph.add_edge("s", "w", 4)
    graph.add_edge("v", "w", 2)
    graph.add_edge("t", "t", 6)
    graph.add_edge("w", "t", 3)

    return graph


@pytest.fixture
def test_directed_graph_weighted_2():
    graph = DirectedGraph(weighted=True)

    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_node(5)

    graph.add_edge(1, 2, 2)
    graph.add_edge(2, 4, 3)
    graph.add_edge(2, 3, 6)
    graph.add_edge(4, 3, 2)
    graph.add_edge(3, 5, 4)

    return graph

@pytest.fixture
def test_negative_cycle_graph():
    graph = DirectedGraph(weighted=True)

    graph.add_node("s")
    graph.add_node("v")
    graph.add_node("w")
    graph.add_node("x")
    graph.add_node("u")

    graph.add_edge("s", "v", 10)
    graph.add_edge("v", "u", -4)
    graph.add_edge("u", "w", 3)
    graph.add_edge("w", "x", -5)
    graph.add_edge("x", "v", 4)

    return graph