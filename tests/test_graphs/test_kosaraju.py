from graphs.kosaraju import find_strongly_connected_components


def test_kosaraju(test_graph, test_graph_2):
    # assert find_strongly_connected_components(test_graph) == {
    #    "s": 1,
    #    "w": 2,
    #    "v": 3,
    #    "t": 4,
    # }
    assert find_strongly_connected_components(test_graph_2) == {
        1: 1,
        3: 1,
        5: 1,
        2: 2,
        4: 3,
        6: 4,
    }
