import random
from typing import Union
from sort.quicksort import partition


def rselect(array: list[Union[int, float]], i: int) -> Union[int, float]:
    """Select the ith element smallest of a list.
    Be careful as this method works on the input array and modifies it in place.
    Uses the same partition logic as the quicksort algorithm. The partition in rselect
    is always based on a uniformly random pivot selection.

    Args:
        array: The array in which the element is to be selected.
        i: The element order to be selected.

    Raises:
        TypeError: Raised if the element order to be selected is bigger than the length of the list.

    Returns:
        The element of the list corresponding to the order i provided.
    """
    n = len(array)
    if i > n:
        raise TypeError(
            f"Element rank {i} to be selected is greater than the size {n} of the array.\
            Provide a rank lower or equal to the size of the input."
        )
    if n == 0:
        return None
    if n == 1:
        return array[0]

    pivot_index = partition(array, 0, n - 1, "random")
    if pivot_index == i:
        return array[pivot_index]
    elif pivot_index > i:
        return rselect(array[:pivot_index], i)
    else:
        return rselect(array[pivot_index:], i - pivot_index)
