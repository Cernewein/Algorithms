def two_sum(integers: list[int], target_integer: int) -> bool:
    """Function that checks if a sum of two input integers selected in a list can result in the target integer.

    Args:
        integers (list[int]): The list of allowed integers
        target_integer (int): The target integer

    Returns:
        bool: Whether or not a combination exists
    """
    lookup = {}
    for integer in integers:
        lookup[integer] = ""

    for integer in integers:
        if target_integer - integer in lookup:
            return True
    return False
