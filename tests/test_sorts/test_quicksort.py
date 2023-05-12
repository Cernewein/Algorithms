from sorts.quicksort import quicksort, partition


def test_quicksort():
    # Testing the quicksort with random pivot choice
    input_list = [2, 3, 1, 5]
    quicksort(input_list, method="random")
    assert input_list == [1, 2, 3, 5]
    input_list = [207, 101.3, 304, 12.3476, 98.0]
    quicksort(input_list, method="random")
    assert input_list == [12.3476, 98.0, 101.3, 207, 304]

    # Testing the quicksort with median method pivot choice
    input_list = [2, 3, 1, 5]
    quicksort(input_list, method="median")
    assert input_list == [1, 2, 3, 5]
    input_list = [207, 101.3, 304, 12.3476, 98.0]
    quicksort(input_list, method="median")
    assert input_list == [12.3476, 98.0, 101.3, 207, 304]

    # Testing the quicksort with left element chosen as pivot
    input_list = [2, 3, 1, 5]
    quicksort(input_list, method="left")
    assert input_list == [1, 2, 3, 5]
    input_list = [207, 101.3, 304, 12.3476, 98.0]
    quicksort(input_list, method="left")
    assert input_list == [12.3476, 98.0, 101.3, 207, 304]

    # Testing the quicksort with right element chosen as pivot
    input_list = [2, 3, 1, 5]
    quicksort(input_list, method="right")
    assert input_list == [1, 2, 3, 5]
    input_list = [207, 101.3, 304, 12.3476, 98.0]
    quicksort(input_list, method="right")
    assert input_list == [12.3476, 98.0, 101.3, 207, 304]
