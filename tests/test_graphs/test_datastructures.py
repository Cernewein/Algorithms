from graphs.datastructures import (
    MinHeap,
    BinaryTreeNode,
    DirectedGraph,
    DirectedGraph,
)


def test_MinHeap():
    heap = MinHeap()
    heap.insert("a", 10)
    heap.insert("b", 3)
    heap.insert("c", 6)
    heap.insert("d", 5)
    heap.insert("e", 2)
    heap.insert("f", 7)

    assert heap.keys == [2, 3, 6, 10, 5, 7]
    assert heap.nodes == ["e", "b", "c", "a", "d", "f"]

    assert heap.extract_min() == ("e", 2)

    assert heap.keys == [3, 5, 6, 10, 7]
    assert heap.nodes == ["b", "d", "c", "a", "f"]

    heap.delete("d")
    assert heap.keys == [3, 7, 6, 10]
    assert heap.nodes == ["b", "f", "c", "a"]


def test_GraphWeighted(test_graph_weighted):
    assert test_graph_weighted.get_distance("s", "w") == 4


def test_DirectedGraphCycle():
    graph = DirectedGraph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)

    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 1)

    assert graph.is_cyclical() == True


def test_DirectedGraphNoCycle():
    graph = DirectedGraph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)

    graph.add_edge(1, 2)
    graph.add_edge(2, 3)

    assert graph.is_cyclical() == False


def test_UndirectedGraphCycle():
    graph = DirectedGraph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)

    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 1)

    assert graph.is_cyclical() == True


def test_UndirectedGraphNoCycle():
    graph = DirectedGraph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)

    graph.add_edge(1, 2)
    graph.add_edge(2, 3)

    assert graph.is_cyclical() == False


def test_BinaryTreeNode():
    root = BinaryTreeNode(10)
    root.insert(3)
    root.insert(4)
    root.insert(15)
    root.insert(12)
    root.insert(7)
    root.insert(11)

    assert root.select(1) == 3
    assert root.select(7) == 15
    assert root.select(5) == 11
