
from dynamic_programming.bellman_ford import bellman_ford
import numpy as np


def test_bellman_ford(test_directed_graph_weighted, test_directed_graph_weighted_2, test_negative_cycle_graph):
    assert {"s": 0, "v": 1, "w": 3, "t": 6} == bellman_ford(test_directed_graph_weighted, "s")

    assert {1: np.inf, 2: 0, 4: 3, 3: 5, 5: 9} == bellman_ford(test_directed_graph_weighted_2, 2)

    assert {} == bellman_ford(test_negative_cycle_graph, "s")