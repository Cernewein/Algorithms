from graphs.datastructures import SigmaTreeNode, MinHeap
from typing import Hashable


def huffman_code(
    alphabet: list[Hashable], frequencies: list[float | int]
) -> list[SigmaTreeNode]:
    """Generate a huffman encoding for a given alphabet and associated symbol frequencies.

    Args:
        alphabet (list): The list of symbols to encode. The symbols need to be hashable
        frequencies (list): the list of assciated symbol frequencies

    Raises:
        ValueError: If the lists are of different lengths an exception is raised

    Returns:
        list[SigmaTreeNode]: The return value is a list of SigmaTreeNode objects.
                                Each object represents a node in the constructed sigma tree.
                                Each node has left and right childs (None if it is a leaf) The huffman code can then be computed by traversing the tree.
    """
    if len(alphabet) != len(frequencies):
        raise ValueError("Please provide two lists with the same length as input.")

    # Initialise helper data structures.
    # The final node list is the final list of nodes that will be returned.
    # A min heap is used to keep track of the current sub tree frequencies and extracting the min values.
    final_nodes = []
    min_heap = MinHeap()
    for i, symbol in enumerate(alphabet):
        min_heap.insert(SigmaTreeNode(symbol, frequencies[i]), frequencies[i])

    # While there are elements in the heap, we keep on merging the subtrees (represented as nodes)
    while len(min_heap) != 0:
        min_node, min_frequency = min_heap.extract_min()
        final_nodes.append(min_node)
        # If there was only one element remaining in the heap, it was the final root node
        if min_heap.get_number_nodes() == 0:
            return final_nodes
        else:
            second_min_node, second_min_frequency = min_heap.extract_min()
        final_nodes.append(second_min_node)

        # Merging the two smallest subtrees and placing the merged tree into the heap
        merged_symbol = min_node.symbol + second_min_node.symbol
        merged_frequency = min_frequency + second_min_frequency
        merged_node = SigmaTreeNode(merged_symbol, merged_frequency)
        merged_node.left_child = min_node
        merged_node.right_child = second_min_node
        min_heap.add_node(merged_node, merged_frequency)

    return final_nodes
