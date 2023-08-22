from greedy.MST import prim, prim_heap
from graphs.datastructures import UndirectedGraph


def test_prim(test_graph_weighted_2):
    miniminum_spanning_tree = UndirectedGraph(weighted=True)
    miniminum_spanning_tree.add_node(1)
    miniminum_spanning_tree.add_node(2)
    miniminum_spanning_tree.add_node(3)
    miniminum_spanning_tree.add_node(4)
    miniminum_spanning_tree.add_node(5)

    miniminum_spanning_tree.add_edge(1, 2, 2)
    miniminum_spanning_tree.add_edge(2, 4, 3)
    miniminum_spanning_tree.add_edge(4, 3, 2)
    miniminum_spanning_tree.add_edge(3, 5, 4)

    assert miniminum_spanning_tree == prim(test_graph_weighted_2)


def test_prim_heap(test_graph_weighted_2):
    miniminum_spanning_tree = UndirectedGraph(weighted=True)
    miniminum_spanning_tree.add_node(1)
    miniminum_spanning_tree.add_node(2)
    miniminum_spanning_tree.add_node(3)
    miniminum_spanning_tree.add_node(4)
    miniminum_spanning_tree.add_node(5)

    miniminum_spanning_tree.add_edge(1, 2, 2)
    miniminum_spanning_tree.add_edge(2, 4, 3)
    miniminum_spanning_tree.add_edge(4, 3, 2)
    miniminum_spanning_tree.add_edge(3, 5, 4)

    assert miniminum_spanning_tree == prim_heap(test_graph_weighted_2)
