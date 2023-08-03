from greedy.huffman import huffman_code
from graphs.datastructures import SigmaTreeNode


def test_huffman_code():
    # Create a very basic alphabet
    # final tree will be
    #         O
    #       /   \
    #      b     O
    #           /  \
    #           c   a
    alphabet = ["a", "b", "c"]
    frequencies = [3, 6, 1]
    root = SigmaTreeNode("bca", 10)
    right_node = SigmaTreeNode("ca", 4)
    a_node = SigmaTreeNode("a", 3)
    b_node = SigmaTreeNode("b", 6)
    c_node = SigmaTreeNode("c", 1)
    root.left_child = b_node
    root.right_child = right_node
    right_node.left_child = c_node
    right_node.right_child = a_node

    encoded_alphabet = [root, right_node, a_node, b_node, c_node]
    nodes = huffman_code(alphabet, frequencies)
    # Check that the nodes outputted by the huffman encoding are contained in the encoded alphabet built by hand.
    for node in nodes:
        assert node in encoded_alphabet
