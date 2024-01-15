def knapsack_value(values: list[int], weights: list[int], capacity: int) -> int:
    """Return the maximum total value that can be obtained with given objects and knapsack capacity

    Args:
        values (list[int]): The object values
        weights (list[int]): The object weights
        capacity (int): The knapsack capacity

    Returns:
        int: The maximum value that can be put in the knapsack
    """
    num_elements = len(values)
    solution_array = build_knapsack_array(values, weights, capacity)
    return solution_array[num_elements][capacity]


def build_knapsack_array(
    values: list[int], weights: list[int], capacity: int
) -> list[int, int]:
    """Helper function that builds the overall solution array

    Args:
        values (list[int]): The object values
        weights (list[int]): The object weights
        capacity (int): The knapsack capacity

    Raises:
        ValueError: When values and weights are of different size

    Returns:
        list[int, int]: The overall solution array that leads to the optimal solution
    """
    num_elements = len(values)
    if num_elements != len(weights):
        raise ValueError("Values and weights of the objects should be of same size.")

    # Initial values for all combinations is 0
    # Solution array is of dimension (num_elements+1)x(capacity+1)
    # Value for number elements = 2 and capacity = 4 can be accessed via solution_array[1][4]
    solution_array = [[0 for i in range(capacity + 1)] for j in range(num_elements + 1)]

    # Solve all subproblems
    for i in range(1, num_elements + 1):
        for c in range(capacity + 1):
            object_weight = weights[i - 1]
            object_value = values[i - 1]
            if object_weight > c:
                # Object cannot be added to the knapsack
                solution_array[i][c] = solution_array[i - 1][c]
            else:
                # Either the object should be added if it's interesting, or it isn't interesting to add it
                solution_array[i][c] = max(
                    solution_array[i - 1][c],
                    solution_array[i - 1][c - object_weight] + object_value,
                )
    return solution_array


def reconstruct_knapsack(
    values: list[int], weights: list[int], capacity: int
) -> list[int]:
    """Compute the list of object indices in the optimal solution

    Args:
        values (list[int]): The object values
        weights (list[int]): The object weights
        capacity (int): The knapsack capacity

    Returns:
        list[int]: The list of object indices in the optimal solution
    """
    num_elements = len(values)
    solution_array = build_knapsack_array(values, weights, capacity)
    optimal_solution = []
    remaining_capacity = capacity
    for i in range(num_elements, 1, -1):
        object_weight = weights[i - 1]
        object_value = values[i - 1]
        if object_should_be_included(
            object_weight, object_value, i, remaining_capacity, solution_array
        ):
            optimal_solution.append(i - 1)
            remaining_capacity -= object_weight
    return optimal_solution


def object_should_be_included(
    object_weight: int,
    object_value: int,
    object_index: int,
    remaining_capacity: int,
    solution_array: list[int, int],
) -> bool:
    """Helper function that determines if an object is included in the optimal solution based on the provided dynamic programming solution array

    Args:
        object_weight (int): The weight of the object to evaluate
        object_value (int): The value of the object to evaluate
        object_index (int): The solution array index of the object to evaluate
        remaining_capacity (int): The remaining capacity of the knapsack
        solution_array (list[int, int]): The dynamic programming solution array

    Returns:
        bool: Whether or not the object is included in the optimal solution
    """
    return (
        object_weight < remaining_capacity
        and solution_array[object_index - 1][remaining_capacity - object_weight]
        + object_value
        > solution_array[object_index - 1][remaining_capacity]
    )
