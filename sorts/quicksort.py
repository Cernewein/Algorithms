from typing import Union
import random
import statistics


class ArgumentError(Exception):
    pass


def choose_pivot(
    array: list[Union[int, float]], left: int, right: int, method: str
) -> int:
    """Chooses a pivot element for quicksort based on specified method.
    Allowed methods are :
        * 'left' : the leftmost element is chosen as pivot.
        * 'right' : the rightmost element is chosen as pivot.
        * 'random' : a random element is chosen as pivot
        * 'median' : the median value of the three elements [left, right, middle] is chosen as pivot.

    Args:
        array : The array for which a pivot element should be chosen.
        left : The left index for the subarray the method should be working on.
        right  : The right index for the subarray the method should be working on.
        method : The method to be used for pivot selection. Can be one of the four ['left', 'right', 'median', 'random'].

    Raises:
        ArgumentError: Raises an argument error when the selected method is not in the allowed list.

    Returns:
        The chosen pivot index
    """
    if method == "random":
        pivot_index = random.randint(left, right)
    elif method == "left":
        pivot_index = left
    elif method == "right":
        pivot_index = right
    elif method == "median":
        values = []
        values.append(array[left])
        values.append(array[right])
        middle_index = (right - left) // 2
        values.append(array[middle_index])
        median = statistics.median(values)
        if array[left] == median:
            pivot_index = left
        elif array[right] == median:
            pivot_index = right
        else:
            pivot_index = middle_index
    else:
        raise ArgumentError(
            f"{method} method not recognized. Please provide one of the three methods ['left', 'right', 'median', 'random']."
        )
    return pivot_index


def partition(
    array: list[Union[int, float]], left: int, right: int, method: str
) -> int:
    """Partition a subset of an array around a pivot element chosen based on the specified method.
    Elements smaller than the pivot will be placed on the left of the pivot.
    Elements greater than the pivot will be placed on the right of the pivot.
    Modifies the array inplace.

    Args:
        array : The input array to be partitioned
        left : The left index of the array subset
        right : The right index of the array subset
        method : The method to be used for pivot selection. Can be one of the four ['left', 'right', 'median', 'random'].

    Returns:
        The pivot used for partitioning index
    """
    # Choose a random pivot element and place it at the beginning of the array
    pivot_index = choose_pivot(array, left, right, method)
    (array[pivot_index], array[left]) = (array[left], array[pivot_index])
    pivot = array[left]

    # Pointer for the first element greater than the pivot
    i = left + 1

    for j in range(left + 1, right + 1):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i

            (array[i], array[j]) = (array[j], array[i])
            i = i + 1

    # Put the pivot at its place : just before the first element greater than the pivot
    (array[i - 1], array[left]) = (array[left], array[i - 1])

    # Return the position of the pivot element
    return i - 1


def quicksort(
    array: list[Union[int, float]],
    left: Union[int, None] = None,
    right: Union[int, None] = None,
    method: str = "random",
):
    """Sort an array inplace. Uses the quicksort algorithm in order to sort the array and chooses a pivot based on specified method.
    Allowed methods for pivot selection are :
        * 'left' : the leftmost element is chosen as pivot.
        * 'right' : the rightmost element is chosen as pivot.
        * 'random' : a random element is chosen as pivot
        * 'median' : the median value of the three elements [left, right, middle] is chosen as pivot.

    Args:
        array : The input array that should be sorted
        left (optional): The left index of the subarray that should be sorted. Defaults to None and mostly used for recursion.
        right (optional): The right index of the subarray that sould be sorted. Defaults to None and mostly used for recursion.
        method (optional): The method to be used for pivot selection. Can be one of the four ['left', 'right', 'median', 'random'].
    """
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1
    if left < right:
        # Choose a pivot element and partition the array such that
        # elements smaller than pivot are on the left
        # elements greater than pivot are on the right
        pivot = partition(array, left, right, method)

        # Recursive call on the left of pivot
        quicksort(array, left, pivot - 1, method)

        # Recursive call on the right of pivot
        quicksort(array, pivot + 1, right, method)
