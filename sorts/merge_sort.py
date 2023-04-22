def merge(integer_list_1: list[int], integer_list_2: list[int]) -> list[int]:
    """Merges two previously sorted lists of integers into a single sorted list."""
    merged_list = []
    while len(integer_list_1) > 0 and len(integer_list_2) > 0:
        if integer_list_1[0] <= integer_list_2[0]:
            merged_list.append(integer_list_1[0])
            integer_list_1.pop(0)
        else:
            merged_list.append(integer_list_2[0])
            integer_list_2.pop(0)
    if len(integer_list_1) > 0:
        merged_list += integer_list_1
    else:
        merged_list += integer_list_2
    return merged_list

def merge_sort(integer_list: list[int]) -> list[int]:
    """Takes a list of integers as input and returns a sorted list as output.
    The list is sorted based on the MergeSort algorithm."""
    list_length = len(integer_list)
    if list_length <= 1:
        return(integer_list)
    else:
        integer_list_1 = integer_list[0:list_length//2]
        integer_list_2 = integer_list[list_length//2:]
        sorted_integer_list_1 = merge_sort(integer_list_1)
        sorted_integer_list_2 = merge_sort(integer_list_2)
        return(merge(sorted_integer_list_1, sorted_integer_list_2))