from typing import Union, Hashable
import numpy as np


class DirectedGraph:
    """Class that represents a graph using the adjacency list structure"""

    def __init__(self, weighted: bool = False) -> None:
        self.adjacency_list = {}
        self.weighted = weighted

    def add_node(self, node: object) -> None:
        """Add a node to the graph.

        Args:
            node : Name of the node to be added
        """
        if node in self.adjacency_list.keys():
            raise Exception("Node already exists !")
        elif self.weighted:
            self.adjacency_list[node] = {}
        else:
            self.adjacency_list[node] = []

    def add_edge(
        self,
        start_node: object,
        end_node: object,
        weight: Union[int, float, None] = None,
    ) -> None:
        """Add a directed edge to the graph. The two nodes provided as argument have to exist. If they don't they need to be added using add_node

        Args:
            start_node : Starting node for the directed edge
            end_node : End node for the directed edge
            weight : Optional value for weighting an edge
        """
        if not start_node in self.adjacency_list.keys():
            raise Exception(f"Start node {start_node} doesn't exist !")
        elif not end_node in self.adjacency_list.keys():
            raise Exception(f"End node {end_node} doesn't exist !")
        elif weight:
            weight_type = type(weight)
            if weight_type != int and weight_type != float:
                raise TypeError(
                    f"Please provide a weight that is a number. Current type is {type(weight)}."
                )
            self.adjacency_list[start_node][end_node] = weight
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

    def get_nodes_and_weights(self) -> list[tuple]:
        """Returns the list of nodes as a list.

        Returns:
            list: The nodes of the graph.
        """
        return list(self.adjacency_list.items())
    
    def get_incoming_nodes(self, node: object) -> list:
        """Get incoming nodes to provided node.

        Args:
            node: The node for which the incoming nodes should be retrieved.

        Returns:
            list: The incoming nodes list.
        """
        if not node in self.adjacency_list.keys():
            raise Exception(f"Node {node} doesn't exist !")
        elif self.weighted:
            incoming_nodes = [k for k, adjacent_nodes in self.adjacency_list.items() if node in adjacent_nodes.keys()]
            return incoming_nodes
        else:
            incoming_nodes = [k for k, adjacent_nodes in self.adjacency_list.items() if node in adjacent_nodes]
            return incoming_nodes

    def get_adjacent_nodes(self, node: object) -> list:
        """Get adjacent nodes to starting node.

        Args:
            node: The node for which the adjacent nodes should be retrieved.

        Returns:
            list: The adjacent nodes list.
        """
        if not node in self.adjacency_list.keys():
            raise Exception(f"Node {node} doesn't exist !")
        elif self.weighted:
            return list(self.adjacency_list[node].keys())
        else:
            return self.adjacency_list[node]

    def get_adjacent_nodes_and_weights(self, node: object) -> list[tuple]:
        """Get adjacent nodes and weights on the edges outgoing from the starting node.

        Args:
            node: The node for which the adjacent nodes should be retrieved.

        Returns:
            list: The adjacent (nodes, weight) list.
        """
        if not self.weighted:
            raise Exception("Graph is not weighted, cannot return a node,weight pair")
        return list(self.adjacency_list[node].items())

    def get_distance(self, start_node, end_node) -> Union[int, float]:
        if self.weighted:
            try:
                return self.adjacency_list[start_node][end_node]
            except IndexError:
                return np.inf
            except KeyError:
                return np.inf
        else:
            if end_node in self.adjacency_list[start_node]:
                return 1
            else:
                return np.inf

    def visit(self, start_node: object, path: set, visited: set) -> bool:
        """Visit nodes from a starting node using DFS.Utility function for the is_cyclical method. Returns true if a node is visited and was already marked as visited.


        Args:
            start_node (object): The starting node for DFS.
            path (set): Helper variable for keeping track of current path explored by DFS.
            visited (set): Helper variable for keeping track of already visited nodes so a node is only visited once.

        Returns:
            bool: Whether or not a node has been visited and was already marked as visited.
        """
        if start_node in visited:
            return False
        visited.add(start_node)
        path.add(start_node)
        for neighbour in self.get_adjacent_nodes(start_node):
            if neighbour in path or self.visit(neighbour, path, visited):
                return True
        path.remove(start_node)
        return False

    def is_cyclical(self) -> bool:
        """Check if graph contains a cycle using DFS.

        Returns:
            bool: Wheter or not the graph contains a cycle
        """
        path = set()
        visited = set()
        return any(self.visit(node, path, visited) for node in self.get_nodes())

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


class UndirectedGraph:
    """Class that represents a graph using the adjacency list structure"""

    def __init__(self, weighted: bool = False) -> None:
        self.adjacency_list = {}
        self.weighted = weighted

    def add_node(self, node: object) -> None:
        """Add a node to the graph.

        Args:
            node : Name of the node to be added
        """
        if node in self.adjacency_list.keys():
            raise Exception("Node already exists !")
        elif self.weighted:
            self.adjacency_list[node] = {}
        else:
            self.adjacency_list[node] = []

    def add_edge(
        self,
        start_node: object,
        end_node: object,
        weight: Union[int, float, None] = None,
    ) -> None:
        """Add a directed edge to the graph. The two nodes provided as argument have to exist. If they don't they need to be added using add_node

        Args:
            start_node : Starting node for the directed edge
            end_node : End node for the directed edge
            weight : Optional value for weighting an edge
        """
        if not start_node in self.adjacency_list.keys():
            raise Exception(f"Start node {start_node} doesn't exist !")
        elif not end_node in self.adjacency_list.keys():
            raise Exception(f"End node {end_node} doesn't exist !")
        elif weight:
            weight_type = type(weight)
            if weight_type != int and weight_type != float:
                raise TypeError(
                    f"Please provide a weight that is a number. Current type is {type(weight)}."
                )
            if weight < 0:
                raise TypeError("Only positive edge weigths are allowed.")
            self.adjacency_list[start_node][end_node] = weight
            self.adjacency_list[end_node][start_node] = weight
        else:
            self.adjacency_list[start_node].append(end_node)
            self.adjacency_list[end_node].append(start_node)

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

    def get_nodes_and_weights(self) -> list[tuple]:
        """Returns the list of nodes as a list.

        Returns:
            list: The nodes of the graph.
        """
        return list(self.adjacency_list.items())

    def get_adjacent_nodes(self, node: object) -> list:
        """Get adjacent nodes to starting node.

        Args:
            node: The node for which the adjacent nodes should be retrieved.

        Returns:
            list: The adjacent nodes list.
        """
        if not node in self.adjacency_list.keys():
            raise Exception(f"Node {node} doesn't exist !")
        elif self.weighted:
            return list(self.adjacency_list[node].keys())
        else:
            return self.adjacency_list[node]

    def get_adjacent_nodes_and_weights(self, node: object) -> list[tuple]:
        """Get adjacent nodes and weights on the edges outgoing from the starting node.

        Args:
            node: The node for which the adjacent nodes should be retrieved.

        Returns:
            list: The adjacent (nodes, weight) list.
        """
        if not self.weighted:
            raise Exception("Graph is not weighted, cannot return a node,weight pair")
        return list(self.adjacency_list[node].items())

    def get_distance(self, start_node, end_node) -> Union[int, float]:
        return self.adjacency_list[start_node][end_node]

    def visit(
        self, start_node: object, parent_node: object | None, path: set, visited: set
    ) -> bool:
        """Visit nodes from a starting node using DFS.Utility function for the is_cyclical method. Returns true if a node is visited and was already marked as visited.


        Args:
            start_node (object): The starting node for DFS.
            path (set): Helper variable for keeping track of current path explored by DFS.
            visited (set): Helper variable for keeping track of already visited nodes so a node is only visited once.

        Returns:
            bool: Whether or not a node has been visited and was already marked as visited.
        """
        if start_node in visited:
            return False
        visited.add(start_node)
        path.add(start_node)
        for neighbour in self.get_adjacent_nodes(start_node):
            if neighbour == parent_node:
                pass
            elif neighbour in path or self.visit(neighbour, start_node, path, visited):
                return True
        path.remove(start_node)
        return False

    def is_cyclical(self) -> bool:
        """Check if graph contains a cycle using DFS.

        Returns:
            bool: Wheter or not the graph contains a cycle
        """
        path = set()
        visited = set()
        return any(self.visit(node, None, path, visited) for node in self.get_nodes())

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


class MinHeap:
    """Class that implements the minHeap data structure. The two essential methods for this data structure are insert and extract_min."""

    def __init__(self) -> None:
        """The nodes list holds the elements and associated keys are stored in the keys list. The keys are the values used for ordering the heap.
        The last added index is an internal memory used in the extract_min function."""
        self.nodes = []
        self.keys = []
        self.node_positions = {}
        self.last_added_index = 0

    def __get_parent(self, index: int) -> int:
        if index == 1:
            return 1
        return index // 2

    def __get_left_child(self, index: int) -> int:
        if index * 2 > self.get_number_nodes():
            return index
        return index * 2

    def __get_right_child(self, index: int) -> int:
        if index * 2 + 1 > self.get_number_nodes():
            return index
        return index * 2 + 1

    def __swap(self, index1: int, index2: int) -> None:
        """Swap two elements in the heap. Swaps both the elements in the nodes list and the associated keys.

        Args:
            index1 (int): Index of the first element to be swapped. Index counting starts at 1 in this datastructure.
            index2 (int): Index of the second element to be swapped. Index counting starts at 1 in this datastructure.
        """
        node1 = self.nodes[index1 - 1]
        node2 = self.nodes[index2 - 1]
        self.node_positions[node1] = index2
        self.node_positions[node2] = index1

        self.nodes[index1 - 1], self.nodes[index2 - 1] = (
            node2,
            node1,
        )

        self.keys[index1 - 1], self.keys[index2 - 1] = (
            self.keys[index2 - 1],
            self.keys[index1 - 1],
        )

    def add_node(self, node: object, key: int) -> None:
        """Add a node to the heap.

        Args:
            node (object): The node to be added. A node represents the object that is stored in the heap.
            key (int): Associated key to be added with the node. The key represents the "weight" or "value" associated to an object and is used for the internal ordering of the heap.

        Raises:
            TypeError: If a key that is not a number is povided this exception is raised.
        """
        self.nodes.append(node)
        try:
            key / 1
        except TypeError:
            raise TypeError(
                "Please provide a key that is either an integer or a real number."
            )
        self.keys.append(key)

    def get_node(self, index: int) -> tuple[object, Union[int, float]]:
        return self.nodes[index - 1], self.keys[index - 1]

    def get_node_key(self, index: int) -> object:
        return self.keys[index - 1]

    def get_last_added_node(self) -> tuple[object, float]:
        return self.nodes.pop(self.last_added_index - 1), self.keys.pop(
            self.last_added_index - 1
        )

    def get_number_nodes(self) -> int:
        return len(self.nodes)

    def get_node_index(self, node) -> int:
        return self.node_positions[node]

    def insert(self, node: object, key: float) -> None:
        """Insert an element into the heap and rearrange the heap so that the order is maintained correctly.

        Args:
            node (object): The element to be added to the heap.
            key (float): The key associated to the element and that will be used for structuring the heap.
        """
        self.add_node(node, key)
        node_index = self.get_number_nodes()
        parent_index = self.__get_parent(node_index)
        while key < self.get_node_key(parent_index):
            self.__swap(node_index, parent_index)
            node_index = parent_index
            parent_index = self.__get_parent(node_index)
        self.last_added_index = node_index
        self.node_positions[node] = node_index

    def bubble_down(self, index: int) -> None:
        # Getting last element index and switching places with the node situated at index provided as input value
        if self.get_number_nodes() == 0:
            return
        if self.get_number_nodes() == 1:
            self.nodes.pop()
            self.keys.pop()
            return
        last_node = self.nodes.pop()
        last_key = self.keys.pop()
        self.nodes[index - 1] = last_node
        self.keys[index - 1] = last_key

        # Checking which elements are now the children of the last element in the heap
        last_index = 1
        left_child_index = self.__get_left_child(last_index)
        right_child_index = self.__get_right_child(last_index)
        # If the children have smaller keys, the positions have to be exchanged.
        while self.get_node_key(last_index) > self.get_node_key(
            left_child_index
        ) or self.get_node_key(last_index) > self.get_node_key(right_child_index):
            # While a children has a lower key value than the last inserted value, the heap is rearranged using bubble down.
            # The swap takes place with the child having the lower key value.
            if self.get_node_key(left_child_index) < self.get_node_key(
                right_child_index
            ):
                self.__swap(last_index, left_child_index)
                last_index = left_child_index
            else:
                self.__swap(last_index, right_child_index)
                last_index = right_child_index
            left_child_index = self.__get_left_child(last_index)
            right_child_index = self.__get_right_child(last_index)

    def delete(self, node: object) -> None:
        index = self.get_node_index(node)
        self.bubble_down(index)

    def extract_min(self) -> object:
        """Extract the element with the minimal key value. After extraction the heap is reordered.

        Returns:
            object: The element with the minimum key value.
        """
        # First extracting the min value and then performing bubble down
        min_node, min_key = self.get_node(1)

        self.bubble_down(1)

        return min_node, min_key

    def __len__(self) -> int:
        return len(self.nodes)


class BinaryTreeNode:
    """A class that is used for building a binary search tree. NB: this tree will most likely not be balanced."""

    def __init__(self, key) -> None:
        self.key = key
        self.left_child = None
        self.right_child = None
        # Subtree size can be used for the selection method
        self.subtree_size = 1

    def insert(self, key: Union[int, float]) -> None:
        """Insert a new node into the binary tree. The tree is recursively traversed until a free spot is found.

        Args:
            key: The new node key to be inserted
        """
        self.subtree_size += 1
        if self.key > key:
            if self.left_child is None:
                self.left_child = BinaryTreeNode(key)
            else:
                self.left_child.insert(key)
        elif self.key < key:
            if self.right_child is None:
                self.right_child = BinaryTreeNode(key)
            else:
                self.right_child.insert(key)

    def select(self, index: int) -> Union[int, float]:
        if self.left_child is not None:
            left_subtree_size = self.left_child.subtree_size
        else:
            left_subtree_size = 0

        if left_subtree_size + 1 == index:
            return self.key
        elif left_subtree_size >= index:
            return self.left_child.select(index)
        elif self.right_child is not None:
            return self.right_child.select(index - left_subtree_size - 1)
        else:
            return None


class SigmaTreeNode:
    """A class representing a node in an alphabet sigma tree. This class can be used to represent a huffman encoding of an alphabet.
    Each SigmaTreeNode has a left/right child (it therfore is structured as a binary tree), a symbol and a frequency.
    """

    def __init__(self, symbol: Hashable, frequency: int | float) -> None:
        """Initialize a node.

        Args:
            symbol (Hashable): The alphabet symbol of the node
            frequency (int | float): The associated symbol frequency
        """
        self.symbol = symbol
        self.frequency = frequency
        self.left_child = None
        self.right_child = None

    def __eq__(self, other) -> bool:
        return (self.symbol, self.frequency, self.left_child, self.right_child) == (
            other.symbol,
            other.frequency,
            other.left_child,
            other.right_child,
        )

    def __repr__(self) -> str:
        left_child_string = self.left_child.symbol if self.left_child else ""
        right_child_string = self.right_child.symbol if self.right_child else ""
        return f"Symbol : {self.symbol}\n Frequency : {self.frequency} \n Left child : {left_child_string} \n Right child : {right_child_string}"

    def __hash__(self) -> int:
        return hash(self.symbol)
