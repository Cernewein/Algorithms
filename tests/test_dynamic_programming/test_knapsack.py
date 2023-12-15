from dynamic_programming.knapsack import knapsack_value, reconstruct_knapsack


def test_knapsack_value():
    values = [3, 2, 4, 4]
    weights = [4, 3, 2, 3]
    capacity = 6

    assert 8 == knapsack_value(values, weights, capacity)


def test_reconstruct_knapsack():
    values = [3, 2, 4, 4]
    weights = [4, 3, 2, 3]
    capacity = 6

    assert [3, 2] == reconstruct_knapsack(values, weights, capacity)
