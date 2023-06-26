class Graph(dict):
    """Class that represents a graph using the adjacency list structure"""

    def __init__(self) -> None:
        self.adjacency_list = {}

    def add_node(self, node: object) -> None:
        """Add a node to the graph.

        Args:
            node : Name of the node to be added
        """
        if node in self.adjacency_list.keys():
            raise Exception("Node already exists !")
        else:
            self.adjacency_list[node] = []

    def add_edge(self, start_node: object, end_node: object) -> None:
        """Add a directed edge to the graph. The two nodes provided as argument have to exist. If they don't they need to be added using add_node

        Args:
            start_node : Starting node for the directed edge
            end_node : End node for the directed edge
        """
        if not start_node in self.adjacency_list.keys():
            raise Exception(f"Start node {start_node} doesn't exist !")
        elif not end_node in self.adjacency_list.keys():
            raise Exception(f"End node {end_node} doesn't exist !")
        else:
            self.adjacency_list[start_node].append(end_node)

    def set_node_and_adjacent_nodes(
        self, start_node: object, adjacent_nodes: list
    ) -> None:
        """Set a node directly with its adjacent node. Please be careful as this method does not check for the existence of the adjacent nodes.

        Args:
            start_node: Initial node
            adjacent_nodes: The adjacent nodes list associated to the initial node.

        """
        if type(adjacent_nodes) != list:
            raise Exception("Please provide an element of type list as adjacent nodes.")
        self.adjacency_list[start_node] = adjacent_nodes

    def get_nodes(self) -> list:
        """Returns the list of nodes as a list.

        Returns:
            list: The nodes of the graph.
        """
        return list(self.adjacency_list.keys())

    def get_adjacent_nodes(self, node: object) -> list:
        """Get adjacent nodes to starting node.

        Args:
            node: The node for which the adjacent nodes should be retrieved.

        Returns:
            list: The adjacent nodes list.
        """
        if not node in self.adjacency_list.keys():
            raise Exception(f"Node {node} doesn't exist !")
        else:
            return self.adjacency_list[node]

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f"{class_name}()"

    def __str__(self) -> str:
        string = "A Graph in adjacency list representation.\n"
        string += "Starting node ---> Connected nodes\n"
        for start_node in self.adjacency_list.keys():
            string += f"\t{start_node} -------> {self.adjacency_list[start_node]}\n"
        return string

    def __eq__(self, other: object) -> bool:
        if type(self) != type(other):
            return False
        equal = set(self.adjacency_list.keys()) == set(other.adjacency_list.keys())
        # Two graphs need to have the same starting_node/adjacent nodes list
        equal = equal and self.adjacency_list == other.adjacency_list
        return equal

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)


def topological_sort(graph: Graph) -> list:
    """Topologically sort a graph. This topological sort uses recursive DFS.

    Args:
        graph: The graph to be topologically sorted.

    Returns:
        list: The list of nodes in topological order.
    """
    nodes_to_explore = graph.get_nodes()
    explored_nodes = set()
    ordered_nodes = []
    for node in nodes_to_explore:
        if node not in explored_nodes:
            explored_nodes, ordered_nodes = recursive_topological_dfs(
                graph, node, explored_nodes, ordered_nodes
            )
    return ordered_nodes[::-1]


def recursive_topological_dfs(
    graph: Graph, start: object, explored_nodes: list, ordered_nodes: list
) -> tuple[list, list]:
    """Helper function for the topological sort of a graph. Handles the recursive DFS part.
    Orders nodes starting from a specific start node and adds these to the preexisting ordered nodes list.

    Args:
        graph: The graph on which to order on.
        start: The starting node for the ordering sequence.
        explored_nodes: The list of already explored nodes.
        ordered_nodes: The list of ordered nodes. NB these are actually in reverse order.

    Returns:
        tuple[list, list]: The updated explored_nodes and ordered_nodes lists.
    """
    explored_nodes.add(start)
    for node in graph.get_adjacent_nodes(start):
        if node not in explored_nodes:
            explored_nodes, ordered_nodes = recursive_topological_dfs(
                graph, node, explored_nodes, ordered_nodes
            )
    ordered_nodes.append(start)
    return explored_nodes, ordered_nodes
