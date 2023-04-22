import math

def karatsuba_multiplication(x: int, y: int) -> int:
    """Takes two integers and returns the result as an integer. 
    Multiplication is computed using the karatsuba algorithm.
    See https://en.wikipedia.org/wiki/Karatsuba_algorithm for more details on the algorithm"""
    n_x = len(str(x))
    n_y = len(str(y))

    if n_x == 1 or n_y == 1:
        return(x*y)

    n = max(n_x, n_y)

    # Splitting both x and y into two n/2-digit numbers so that multiplications
    # can be recursively computed.
    n2 = n//2
    
    first_half_x = x //(10**(n2))
    second_half_x = x % (10**(n2))

    first_half_y = y//10**(n2)
    second_half_y = y % (10**(n2))

    first_halves_multiplication = karatsuba_multiplication(first_half_x, first_half_y)
    second_halves_multiplication = karatsuba_multiplication(second_half_x, second_half_y)
    sum_multiplication = karatsuba_multiplication(first_half_x + second_half_x, first_half_y + second_half_y)

    intermediate_numbers = sum_multiplication - first_halves_multiplication - second_halves_multiplication

    return((10**(2*n2)) * round(first_halves_multiplication) + (10**(n2)) * round(intermediate_numbers) + round(second_halves_multiplication))