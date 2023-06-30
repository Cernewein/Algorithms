from graphs.dijkstra import dijkstra


def test_dijkstra(test_graph_weighted):
    assert {"s": 0, "v": 1, "w": 3, "t": 6} == dijkstra(test_graph_weighted, "s")
