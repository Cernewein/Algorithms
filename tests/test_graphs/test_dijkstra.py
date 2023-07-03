from graphs.dijkstra import dijkstra, dijkstra_heap


def test_dijkstra(test_graph_weighted, test_graph_weighted_2):
    assert {"s": 0, "v": 1, "w": 3, "t": 6} == dijkstra(test_graph_weighted, "s")

    assert {1: 1e7, 2: 0, 4: 3, 3: 5, 5: 9} == dijkstra(test_graph_weighted_2, 2)


def test_dijkstra_heap(test_graph_weighted, test_graph_weighted_2):
    assert {"s": 0, "v": 1, "w": 3, "t": 6} == dijkstra_heap(test_graph_weighted, "s")

    assert {1: 1e7, 2: 0, 4: 3, 3: 5, 5: 9} == dijkstra_heap(test_graph_weighted_2, 2)
