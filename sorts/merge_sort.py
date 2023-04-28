from typing import Union


def merge(
    input_list_1: list[Union[float, int]], input_list_2: list[Union[float, int]]
) -> list[Union[float, int]]:
    """Merges two previously sorted lists into a single sorted list."""
    merged_list = []
    while len(input_list_1) > 0 and len(input_list_2) > 0:
        if input_list_1[0] <= input_list_2[0]:
            merged_list.append(input_list_1[0])
            input_list_1.pop(0)
        else:
            merged_list.append(input_list_2[0])
            input_list_2.pop(0)
    if len(input_list_1) > 0:
        merged_list += input_list_1
    else:
        merged_list += input_list_2
    return merged_list


def merge_sort(input_list: list[Union[float, int]]) -> list[Union[float, int]]:
    """Takes a list of numbers as input and returns a sorted list as output.
    The list is sorted based on the MergeSort algorithm."""
    list_length = len(input_list)
    if list_length <= 1:
        return input_list
    else:
        input_list_1 = input_list[0 : list_length // 2]
        input_list_2 = input_list[list_length // 2 :]
        sorted_input_list_1 = merge_sort(input_list_1)
        sorted_input_list_2 = merge_sort(input_list_2)
        return merge(sorted_input_list_1, sorted_input_list_2)


def merge_and_count_split_inversions(
    input_list_1: list[Union[float, int]], input_list_2: list[Union[float, int]]
) -> tuple[list[Union[float, int]], int]:
    """Merges two previously sorted lists into a single sorted list and also returns the number of split inversions found.
    The return value is a tuple (sorted_list, number_split_inversions)."""
    merged_list = []
    split_inversions = 0
    while len(input_list_1) > 0 and len(input_list_2) > 0:
        if input_list_1[0] <= input_list_2[0]:
            merged_list.append(input_list_1[0])
            input_list_1.pop(0)
        else:
            merged_list.append(input_list_2[0])
            input_list_2.pop(0)
            split_inversions += len(input_list_1)
    if len(input_list_1) > 0:
        merged_list += input_list_1
    else:
        merged_list += input_list_2
    return merged_list, split_inversions


def merge_sort_and_count_split_inversions(
    input_list: list[Union[float, int]]
) -> tuple[list[Union[float, int]], int]:
    """Takes a list of numbers as input and returns a sorted list as well as the number of inversions in that list as output.
    The list is sorted based on the MergeSort algorithm."""
    list_length = len(input_list)
    if list_length <= 1:
        return input_list, 0
    else:
        input_list_1 = input_list[0 : list_length // 2]
        input_list_2 = input_list[list_length // 2 :]
        sorted_input_list_1, left_inversions = merge_sort_and_count_split_inversions(
            input_list_1
        )
        sorted_input_list_2, right_inversions = merge_sort_and_count_split_inversions(
            input_list_2
        )
        sorted_list, split_inversions = merge_and_count_split_inversions(
            sorted_input_list_1, sorted_input_list_2
        )
        inversions = split_inversions + left_inversions + right_inversions
        return sorted_list, inversions
