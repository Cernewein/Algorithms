
from dynamic_programming.floyd_warshall import floyd_warhsall
import numpy as np


def test_bellman_ford(test_directed_graph_weighted, test_directed_graph_weighted_2, test_negative_cycle_graph):
    assert {("s","s"): 0, ("s","v"): 1, ("s","w"): 3, ("s","t"): 6,
            ("t", "s") : np.inf, ("t", "v") : np.inf, ("t", "w") : np.inf, ("t", "t") : 0,
            ("v","s"): np.inf, ("v","v"): 0, ("v","w"): 2, ("v","t"): 5,
            ("w","s"): np.inf, ("w","v"): np.inf, ("w","w"): 0, ("w","t"): 3,} == floyd_warhsall(test_directed_graph_weighted)

    assert {} == floyd_warhsall(test_negative_cycle_graph)