from sort.quicksort import quicksort, partition, choose_pivot
import random


def test_quicksort():
    # Testing the quicksort with random pivot choice
    input_list = [2, 3, 1, 5]
    quicksort(input_list, method="random")
    assert input_list == [1, 2, 3, 5]
    input_list = [207, 101.3, 304, 12.3476, 98.0]
    quicksort(input_list, method="random")
    assert input_list == [12.3476, 98.0, 101.3, 207, 304]
    input_list = []
    quicksort(input_list, method="random")
    assert input_list == []
    input_list = [2]
    quicksort(input_list, method="random")
    assert input_list == [2]

    # Testing the quicksort with median method pivot choice
    input_list = [2, 3, 1, 5]
    quicksort(input_list, method="median")
    assert input_list == [1, 2, 3, 5]
    input_list = [207, 101.3, 304, 12.3476, 98.0]
    quicksort(input_list, method="median")
    assert input_list == [12.3476, 98.0, 101.3, 207, 304]
    # Edge cases
    input_list = []
    quicksort(input_list, method="median")
    assert input_list == []
    input_list = [2]
    quicksort(input_list, method="median")
    assert input_list == [2]

    # Testing the quicksort with left element chosen as pivot
    input_list = [2, 3, 1, 5]
    quicksort(input_list, method="left")
    assert input_list == [1, 2, 3, 5]
    input_list = [207, 101.3, 304, 12.3476, 98.0]
    quicksort(input_list, method="left")
    assert input_list == [12.3476, 98.0, 101.3, 207, 304]
    # Edge cases
    input_list = []
    quicksort(input_list, method="left")
    assert input_list == []
    input_list = [2]
    quicksort(input_list, method="left")
    assert input_list == [2]

    # Testing the quicksort with right element chosen as pivot
    input_list = [2, 3, 1, 5]
    quicksort(input_list, method="right")
    assert input_list == [1, 2, 3, 5]
    input_list = [207, 101.3, 304, 12.3476, 98.0]
    quicksort(input_list, method="right")
    assert input_list == [12.3476, 98.0, 101.3, 207, 304]
    # Edge cases
    input_list = []
    quicksort(input_list, method="right")
    assert input_list == []
    input_list = [2]
    quicksort(input_list, method="right")
    assert input_list == [2]


def test_choose_pivot():
    array = [207, 101.3, 304, 12.3476, 98.0]
    left = 1
    right = 3
    assert 1 == choose_pivot(array, left, right, "left")
    assert 3 == choose_pivot(array, left, right, "right")
    assert 1 == choose_pivot(array, left, right, "median")

    assert 1 <= choose_pivot(array, left, right, "random")
    assert 3 >= choose_pivot(array, left, right, "random")
    random.seed(0)
    assert 2 == choose_pivot(array, left, right, "random")


def test_partition():
    array = [207, 101.3, 304, 12.3476, 98.0]
    left = 0
    right = 4
    pivot_index = partition(array, left, right, "left")
    assert array == [98.0, 101.3, 12.3476, 207, 304]
    assert pivot_index == 3

    array = [207, 101.3, 304, 12.3476, 98.0]
    left = 0
    right = 4
    pivot_index = partition(array, left, right, "right")
    assert array == [12.3476, 98.0, 304, 101.3, 207]
    assert pivot_index == 1

    array = [207, 101.3, 304, 12.3476, 98.0]
    left = 0
    right = 4
    pivot_index = partition(array, left, right, "median")
    assert array == [98.0, 101.3, 12.3476, 207, 304]
    assert pivot_index == 3

    array = [207, 101.3, 304, 12.3476, 98.0]
    left = 0
    right = 4
    random.seed(0)
    pivot_index = partition(array, left, right, "random")
    assert array == [12.3476, 101.3, 304, 207, 98.0]
    assert pivot_index == 0
