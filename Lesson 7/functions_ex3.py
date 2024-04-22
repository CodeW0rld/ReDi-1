"""
Filtering even numbers demonstration.
"""
def is_even(num):
    """
    Check if a number is even.

    Args:
        num: The number to check.

    Returns:
        True if the number is even, False otherwise.
    """
    return num % 2 == 0

numbers = [1, 2, 4, 5, 6, 7, 8, 11, 17]

filtered_numbers = list(filter(is_even, numbers))

print(filtered_numbers)
