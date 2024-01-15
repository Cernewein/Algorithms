from graphs.datastructures import BinaryTreeNode

def optBST(frequencies: list[int|float]) -> float:
    """This function computes the minimum search time associated to the optimal binary search tree built from given elements with given frequencies.
    Uses dynamic programming for solving this problem.
    The optimal tree is built using the element indices as keys for the tree nodes.

    Args:
        frequencies (list[int | float]): The loockup frequencies associated to each element

    Raises:
        IndexError

    Returns:
        float: The minimum search time associated to the optimal binary search tree.
    """
    num_elements = len(frequencies)
    
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
    return solution_array[0][num_elements-1]

def optBSTKnuth(frequencies: list[int|float]) -> (float, dict):
    """This function builds upon optBST but adds Knuth's optimization for reducing the running time from O(n^3) to O(n^2).
    The main idea is that not all possible roots need to be inspected, by only those situated between the two subtree roots 
    (as otherwise the elements are already contained in on of the two subtrees, there is therefore no need to inspect them).
    Also returns the optimal roots for each subproblem. The optimal roots are the indices of the elements starting with 0.
    The optimal tree is built using the element indices as keys for the tree nodes.
s
    Args:
        frequencies (list[int | float]): The loockup frequencies associated to each element

    Raises:
        IndexError

    Returns:
        float: The minimum search time associated to the optimal binary search tree.
        dict: The dictionnary storing all optimal roots for given subproblems
    """
    num_elements = len(frequencies)
    
    # Initialize the solution array
    solution_array = [[0 for i in range(num_elements + 1)] for j in range(num_elements + 1)]
    subtree_roots = {}


    # Fill out the solution array starting from the diagonal towards the north-west
    for problem_size in range(0, num_elements):
        for i in range(0, num_elements - problem_size):
            min_subtree_search_time = 1000000000
            has_found_min = False
            start_root = subtree_roots.get((i, i + problem_size - 1))
            end_root = subtree_roots.get((i + 1, i + problem_size))
            if start_root == None:
                start_root = i
            if end_root == None:
                end_root = problem_size + i
            for r in range(start_root, end_root + 1):
                # Looking for the root generating the smallest overall search time stemming from two subtrees associated to the selected root.
                try:
                    subtree_search_time = solution_array[i][r - 1] + solution_array[r + 1][i + problem_size]
                except IndexError:
                    # Handling the case when r + i is greater than the number of elements. ie. when the inspected root would only have a left subtree
                    subtree_search_time = solution_array[i][r - 1]
                if min_subtree_search_time > subtree_search_time:
                    min_subtree_search_time = subtree_search_time
                    subtree_roots[(i,i + problem_size)] = r
                    has_found_min = True
            if has_found_min:
                solution_array[i][i + problem_size] = sum(frequencies[(i):(i + problem_size + 1)]) + min_subtree_search_time
            else:
                solution_array[i][i + problem_size] = sum(frequencies[(i):(i + problem_size + 1)])

    return solution_array[0][num_elements-1], subtree_roots

def reconstruct_optBSTKnuth(frequencies: list[int|float]) -> BinaryTreeNode:
    """Compute the optimal binary search tree for given set of keys and frequencies. First uses dynamic programming with Knuth's optimization to find the whole solution array.
    Then reconstruct the optimal search tree by tracing back through the solution array.

    Args:
        frequencies (list[int | float]): The loockup frequencies associated to each element
    Returns:
        BinaryTreeNode: The optimal binary search tree. The optimal tree is built using the element indices as keys for the tree nodes.
    """
    # First compute the optimal solution array and subtree roots
    _, subtree_roots = optBSTKnuth(frequencies)
    num_elements = len(frequencies)
    # initialize the optimal tree
    initial_root = subtree_roots.get((0, num_elements - 1))
    optimal_tree = BinaryTreeNode(initial_root + 1)
    roots_to_explore = []
    left_root = subtree_roots.get((0, initial_root - 1))
    right_root = subtree_roots.get((initial_root + 1, num_elements - 1))
    # Storing the two children in the roots to explore triplet array
    # A triplet to explore is made up of the root and left and right limits of the subproblem the root is an optimal solution of.
    if left_root != None:
        roots_to_explore.append([left_root, 0, initial_root - 1])
    if right_root != None:
        roots_to_explore.append([right_root, initial_root + 1, num_elements - 1])
    # Trace back through the solution to build the optimal tree
    # Uses a queue for storing which roots need to be explored next (finding which children it has)
    while len(roots_to_explore) != 0:
        explored_triplet = roots_to_explore.pop()
        explored_root = explored_triplet[0]
        left_index = explored_triplet[1]
        right_index = explored_triplet[2]
        # Need to increment value with 1 because keys are indexed from 1 and not from 0
        optimal_tree.insert(explored_root + 1)
        left_root = subtree_roots.get((left_index, explored_root - 1))
        right_root = subtree_roots.get((explored_root + 1, right_index))
        if left_root != None:
            roots_to_explore.append([left_root, left_index, explored_root - 1])
        if right_root != None:
            roots_to_explore.append([right_root, explored_root + 1, right_index])
    return optimal_tree