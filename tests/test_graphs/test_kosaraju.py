from graphs.kosaraju import (
    strongly_connected_component_dfs,
    find_strongly_connected_components,
    reverse_graph,
)


def test_find_strongly_connected_components(test_graph, test_graph_2):
    """GIVEN an input graph, test that the SCCs are correctly identified when calling find_strongly_connected_components."""
    scc_test_graph = find_strongly_connected_components(test_graph)
    assert len(set(scc_test_graph.values())) == 4

    scc_test_graph_2 = find_strongly_connected_components(test_graph_2)
    assert scc_test_graph_2[1] == scc_test_graph_2[3] == scc_test_graph_2[5]
    assert len(set(scc_test_graph_2.values())) == 4


def test_strongly_connected_component_dfs(test_graph, test_graph_2):
    """GIVEN an input graph, test that the current SCC is correctly explored when calling strongly_connected_component_dfs."""
    (
        strongly_connected_components,
        explored_nodes,
    ) = strongly_connected_component_dfs(test_graph, "v", 1, {}, set())

    assert explored_nodes == set(["v", "t"])
    assert strongly_connected_components == {"v": 1, "t": 1}

    (
        strongly_connected_components,
        explored_nodes,
    ) = strongly_connected_component_dfs(test_graph_2, 4, 2, {6: 1}, set([6]))

    assert explored_nodes == set([4, 6])
    assert strongly_connected_components == {6: 1, 4: 2}


def test_reverse_graph(test_graph, reverse_test_graph):
    """GIVEN an input graph test that it is correctly reversed when calling reverse_graph."""
    assert reverse_graph(test_graph) == reverse_test_graph
