from greedy.nearest_neighbor_tsp import nearest_neighbor_tsp
from graphs.datastructures import UndirectedGraph


def test_nearest_neighbor_tsp():
    locations_graph = UndirectedGraph(weighted=True)
    locations_graph.add_node("a")
    locations_graph.add_node("b")
    locations_graph.add_node("c")
    locations_graph.add_node("d")
    locations_graph.add_node("e")
    locations_graph.add_edge("a", "b", 1)
    locations_graph.add_edge("a", "c", 4)
    locations_graph.add_edge("a", "d", 5)
    locations_graph.add_edge("a", "e", 10)
    locations_graph.add_edge("b", "c", 2)
    locations_graph.add_edge("b", "d", 6)
    locations_graph.add_edge("b", "e", 3)
    locations_graph.add_edge("c", "d", 7)
    locations_graph.add_edge("c", "e", 8)
    locations_graph.add_edge("d", "e", 9)
    expected_tour = UndirectedGraph(weighted=True)
    expected_tour.add_node("a")
    expected_tour.add_node("b")
    expected_tour.add_node("c")
    expected_tour.add_node("d")
    expected_tour.add_node("e")
    expected_tour.add_edge("a", "b", 1)
    expected_tour.add_edge("b", "c", 2)
    expected_tour.add_edge("c", "d", 7)
    expected_tour.add_edge("d", "e", 9)
    expected_tour.add_edge("e", "a", 10)
    tsp_tour = nearest_neighbor_tsp(locations_graph, "a")

    assert tsp_tour == expected_tour
