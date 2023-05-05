from sorts.merge_sort import (
    merge_sort,
    merge,
    merge_sort_and_count_inversions,
    merge_and_count_split_inversions,
)


def test_merge_sort():
    input_list = [207, 101.3, 304, 12.3476, 98.0]
    assert merge_sort(input_list) == [12.3476, 98.0, 101.3, 207, 304]


def test_merge():
    input_list_1 = [1, 3, 5, 6, 7, 10]
    input_list_2 = [2, 4, 8, 9]
    assert merge(input_list_1, input_list_2) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_merge_sort_and_count_inversion():
    input_list = [207, 101.3, 304, 12.3476, 98.0]
    sorted_list, number_inversion = merge_sort_and_count_inversions(input_list)
    assert sorted_list == [12.3476, 98.0, 101.3, 207, 304]
    assert number_inversion == 3 + 2 + 2


def test_merge_and_count_split_inversion():
    input_list_1 = [1, 3, 5, 6, 7, 10]
    input_list_2 = [2, 4, 8, 9]
    merged_list, number_inversion = merge_and_count_split_inversions(
        input_list_1, input_list_2
    )
    assert merged_list == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert number_inversion == 5 + 4 + 1 + 1
