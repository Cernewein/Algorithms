from dynamic_programming.binary_search_tree import *

def test_optBST_value():
    # Case when all frequencies are equal
    # Here the optimal tree is a balanced one
    #    1
    #   / \
    #  2   3
    keys = [1, 2, 3]
    frequencies = [1, 1, 1]

    assert 5 == optBST(keys, frequencies)

    # Case when frequencies are different from one another
    # Here the otimal tree is a linear tree 1 -> 2 -> 3
    keys = [1, 2, 3]
    frequencies = [0.8, 0.1, 0.1]

    assert 1.3 == optBST(keys, frequencies)

