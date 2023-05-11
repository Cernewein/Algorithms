from sorts.quicksort import quicksort, partition


def test_quicksort():
    input_list = [2, 3, 1, 5]
    quicksort(input_list)
    assert input_list == [1, 2, 3, 5]
    input_list = [207, 101.3, 304, 12.3476, 98.0]
    quicksort(input_list)
    assert input_list == [12.3476, 98.0, 101.3, 207, 304]
