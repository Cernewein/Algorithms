from graphs.median import RunningMedianHeap


def test_RunningMedianHeap():
    running_median = RunningMedianHeap()
    running_median.insert(2)
    running_median.insert(6)
    running_median.insert(5)
    running_median.insert(1274)
    running_median.insert(45)

    assert running_median.get_median() == 6
