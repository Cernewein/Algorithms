from graphs.two_sum import two_sum


def test_two_sum():
    integers = [-3, -1, 1, 2, 9, 11, 7, 6, 2]
    target = 9
    assert two_sum(integers, target)

    integers = [-3, -1, 1, 9, 11, 6, 2]
    target = 9
    assert not two_sum(integers, target)
