from typing import Union
import random


def partition(array: list[Union[int, float]], left: int, right: int) -> int:
    """Partition a subset of an array around a random pivot element.
    Elements smaller than the pivot will be placed on the left of the pivot.
    Elements greater than the pivot will be placed on the right of the pivot.
    Modifies the array inplace.

    Args:
        array : The input array to be partitioned
        left : The left index of the array subset
        right : The right index of the array subset

    Returns:
        The pivot used for partitioning index
    """
    # Choose a random pivot element and place it at the beginning of the array
    pivot_index = random.randint(left, right)
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
):
    """Sort an array inplace. Uses the randomized quicksort algorithm in order to sort the array.

    Args:
        array : The input array that should be sorted
        left (optional): The left index of the subarray that should be sorted. Defaults to None and mostly used for recursion.
        right (optional): The right index of the subarray that sould be sorted. Defaults to None and mostly used for recursion.
    """
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1
    if left < right:
        # Choose a pivot element and partition the array such that
        # elements smaller than pivot are on the left
        # elements greater than pivot are on the right
        pivot = partition(array, left, right)

        # Recursive call on the left of pivot
        quicksort(array, left, pivot - 1)

        # Recursive call on the right of pivot
        quicksort(array, pivot + 1, right)
