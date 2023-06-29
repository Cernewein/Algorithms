from graphs.combinations import combinations, combinations_with_replacement
import pytest
from errors.errors import ArgumentError


def test_combinations():
    # Testing the base case
    number_elements = 1
    l = [1, 2, 3, 4]

    assert [[1], [2], [3], [4]] == combinations(l, number_elements)

    # Testing with more elements to combine
    number_elements = 2
    l = [1, 2, 3, 4]

    assert [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]] == combinations(
        l, number_elements
    )

    # Testing with all elements selected

    number_elements = 4
    l = [1, 2, 3, 4]

    assert [[1, 2, 3, 4]] == combinations(l, number_elements)

    # Number of elements greater than the length of the list
    number_elements = 5
    l = [1, 2, 3, 4]

    with pytest.raises(
        TypeError,
        match=f"Number of elements {number_elements} exceeds the length of the list {len(l)}",
    ):
        combinations(l, number_elements)

    # Number of elements negative
    number_elements = -5
    l = [1, 2, 3, 4]

    with pytest.raises(
        TypeError,
        match="Number of element cannot be negative.",
    ):
        combinations(l, number_elements)

    # Number of elements cannot be a float
    number_elements = 3.2
    l = [1, 2, 3, 4]

    with pytest.raises(TypeError, match="Number of elements cannot be a float."):
        combinations(l, number_elements)


def test_combinations_with_replacement():
    # Testing the base case
    number_elements = 1
    l = [1, 2, 3, 4]

    assert [[1], [2], [3], [4]] == combinations_with_replacement(l, number_elements)

    # Testing with more elements to combine
    number_elements = 2
    l = [1, 2, 3, 4]

    assert [
        [1, 1],
        [1, 2],
        [1, 3],
        [1, 4],
        [2, 2],
        [2, 3],
        [2, 4],
        [3, 3],
        [3, 4],
        [4, 4],
    ] == combinations_with_replacement(l, number_elements)

    # Number of elements greater than the length of the list
    number_elements = 3
    l = [1, 2]

    assert [
        [1, 1, 1],
        [1, 1, 2],
        [1, 2, 2],
        [2, 2, 2],
    ] == combinations_with_replacement(l, number_elements)

    # Number of elements negative
    number_elements = -5
    l = [1, 2, 3, 4]

    with pytest.raises(
        TypeError,
        match="Number of element cannot be negative.",
    ):
        combinations_with_replacement(l, number_elements)

    # Number of elements cannot be a float
    number_elements = 3.2
    l = [1, 2, 3, 4]

    with pytest.raises(TypeError, match="Number of elements cannot be a float."):
        combinations_with_replacement(l, number_elements)
