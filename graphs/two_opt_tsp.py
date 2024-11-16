from graphs.datastructures import UndirectedGraph
from greedy.nearest_neighbor_tsp import nearest_neighbor_tsp

def two_opt_tsp(locations_graph:UndirectedGraph, starting_node:object) -> UndirectedGraph:
    # Creating an initial tour
    tsp_tour = nearest_neighbor_tsp(locations_graph, starting_node)
