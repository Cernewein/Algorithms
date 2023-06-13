from typing import Union
from errors.errors import ArgumentError


def combinations(
    collection: list, number_elements: int, recursion: bool = False
) -> list:
    """Generate all combinations given a collection of elements and the desired number of elements to be combined.
    Uses DFS to generate all combinations.

    Args:
        collection: The input list of elements to be combined
        number_elements : The number of elements in a combination

    Returns:
        Returns a list containing all possible combinations of number_elements made up of elements in collection
    """
    if number_elements == 0:
        return [collection]
    if number_elements == 1:
        return [[element] for element in collection]

    if number_elements < 0:
        raise ArgumentError("Number of element cannot be negative.")

    if number_elements % 1 != 0:
        raise ArgumentError("Number of elements cannot be a float.")

    if (number_elements > len(collection)) & (not recursion):
        raise ArgumentError(
            f"Number of elements {number_elements} exceeds the length of the list {len(collection)}"
        )

    result = []
    for n, element in enumerate(collection[:-1]):
        subsets = [
            sub
            for sub in combinations(collection[(n + 1) :], number_elements - 1, True)
        ]
        for subset in subsets:
            result.append([element] + subset)
    return result
