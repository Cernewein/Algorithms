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


class MinHeap:
    """Class that implements the minHeap data structure. The two essential methods for this data structure are insert and extract_min."""

    def __init__(self) -> None:
        """The nodes list holds the elements and associated keys are stored in the keys list. The keys are the values used for ordering the heap.
        The last added index is an internal memory used in the extract_min function."""
        self.nodes = []
        self.keys = []
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
        self.nodes[index1 - 1], self.nodes[index2 - 1] = (
            self.nodes[index2 - 1],
            self.nodes[index1 - 1],
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

    def get_node(self, index: int) -> object:
        return self.nodes[index - 1]

    def get_node_key(self, index: int) -> object:
        return self.keys[index - 1]

    def get_last_added_node(self) -> tuple[object, float]:
        return self.nodes.pop(self.last_added_index - 1), self.keys.pop(
            self.last_added_index - 1
        )

    def get_number_nodes(self) -> int:
        return len(self.nodes)

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

    def extract_min(self) -> object:
        """Extract the element with the minimal key value. After extraction the heap is reordered.

        Returns:
            object: The element with the minimum key value.
        """
        # First extracting the min value and replacing it with the last element that was inserted into the heap
        min_node = self.get_node(1)
        last_added_element, last_added_element_key = self.get_last_added_node()
        self.nodes[0] = last_added_element
        self.keys[0] = last_added_element_key
        # Checking which elements are now the children of the last element added
        last_added_element_index = 1
        left_child_index = self.__get_left_child(last_added_element_index)
        right_child_index = self.__get_right_child(last_added_element_index)
        # If the children have smaller keys, the positions have to be exchanged.
        while self.get_node_key(last_added_element_index) > self.get_node_key(
            left_child_index
        ) or self.get_node_key(last_added_element_index) > self.get_node_key(
            right_child_index
        ):
            # While a children has a lower key value than the last inserted value, the heap is rearranged using bubble down.
            # The swap takes place with the child having the lower key value.
            if self.get_node_key(left_child_index) < self.get_node_key(
                right_child_index
            ):
                self.__swap(last_added_element_index, left_child_index)
                last_added_element_index = left_child_index
            else:
                self.__swap(last_added_element_index, right_child_index)
                last_added_element_index = right_child_index
            left_child_index = self.__get_left_child(last_added_element_index)
            right_child_index = self.__get_right_child(last_added_element_index)
        return min_node
