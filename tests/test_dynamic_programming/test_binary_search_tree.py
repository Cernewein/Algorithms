from dynamic_programming.binary_search_tree import *

def test_optBST_value():
    # Case when all frequencies are equal
    # Here the optimal tree is a balanced one
    #    2
    #   / \
    #  1   3
    frequencies = [1, 1, 1]

    assert 5 == optBST(frequencies)

    # Case when frequencies are different from one another
    # Here the otimal tree is a linear tree 1 -> 2 -> 3
    frequencies = [0.8, 0.1, 0.1]

    assert 1.3 == optBST(frequencies)


def test_optBSTKnuth_value():
    # Case when all frequencies are equal
    # Here the optimal tree is a balanced one
    #    2
    #   / \
    #  1   3
    frequencies = [1, 1, 1]

    average_frequency, roots = optBSTKnuth(frequencies)
    assert 5 == average_frequency

    # Case when frequencies are different from one another
    # Here the otimal tree is a linear tree 1 -> 2 -> 3
    frequencies = [0.8, 0.1, 0.1]
    average_frequency, roots = optBSTKnuth(frequencies)

    assert 1.3 == average_frequency

def test_reconstruct_optBSTKnuth():
    # Case when all frequencies are equal
    # Here the optimal tree is a balanced one
    #    2
    #   / \
    #  1   3
    frequencies = [1, 1, 1]


    optimal_tree = reconstruct_optBSTKnuth(frequencies)
    assert optimal_tree.key == 2
    assert optimal_tree.left_child.key == 1
    assert optimal_tree.right_child.key == 3

    # Case when frequencies are different from one another
    # Here the otimal tree is a linear tree 1 -> 2 -> 3
    frequencies = [0.8, 0.1, 0.1]
    optimal_tree = reconstruct_optBSTKnuth(frequencies)
    assert optimal_tree.key == 1
    assert optimal_tree.left_child == None
    assert optimal_tree.right_child.key == 2
    assert optimal_tree.right_child.right_child.key == 3
