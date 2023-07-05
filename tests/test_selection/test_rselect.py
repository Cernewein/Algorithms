from selection.rselect import rselect
import pytest


def test_rselect():
    array = [207, 101.3, 304, 12.3476, 98.0]
    i = 2
    assert rselect(array, i) == 101.3

    # Edge cases
    array = []
    assert rselect(array, 0) is None

    array = [1]
    assert rselect(array, 0) == 1

    array = [1]
    i = 10
    n = len(array)
    with pytest.raises(
        TypeError,
        match=f"Element rank {i} to be selected is greater than the size {n} of the array.\
            Provide a rank lower or equal to the size of the input.",
    ):
        rselect(array, i)
