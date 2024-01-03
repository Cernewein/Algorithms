def optBST(keys: list[str|int|float], frequencies: list[int|float]) -> float:
    """This function computes the minimum search time associated to the optimal binary search tree built from given elements with given frequencies.
    Uses dynamic programming for solving this problem.
    The keys denote the place of the element in the overall ordering of the elements. This function assumes that the keys are ordered from smallest to biggest.

    Args:
        keys (list[str | int | float]): The elements to order
        frequencies (list[int | float]): The loockup frequencies associated to each element

    Raises:
        IndexError

    Returns:
        float: The minimum search time associated to the optimal binary search tree.
    """
    num_elements = len(keys)
    if num_elements != len(frequencies):
        raise IndexError("Please provide two arrays of the same length.")
    
    # Initialize the solution array
    solution_array = [[0 for i in range(num_elements + 1)] for j in range(num_elements + 1)]

    # Fill out the solution array starting from the diagonal towards the north-west
    for problem_size in range(0, num_elements):
        for i in range(0, num_elements - problem_size):
            min_subtree_search_time = 1000000000
            has_found_min = False
            for r in range(i, problem_size + i + 1):
                # Looking for the root generating the smallest overall search time stemming from two subtrees associated to the selected root.
                try:
                    subtree_search_time = solution_array[i][r - 1] + solution_array[r + 1][i + problem_size]
                except IndexError:
                    # Handling the case when r + i is greater than the number of elements. ie. when the inspected root would only have a left subtree
                    # This special case
                    subtree_search_time = solution_array[i][r - 1]
                if min_subtree_search_time > subtree_search_time:
                    min_subtree_search_time = subtree_search_time
                    has_found_min = True
            if has_found_min:
                solution_array[i][i + problem_size] = sum(frequencies[(i):(i + problem_size + 1)]) + min_subtree_search_time
            else:
                solution_array[i][i + problem_size] = sum(frequencies[(i):(i + problem_size + 1)])
    print(solution_array)
    return solution_array[0][num_elements-1]