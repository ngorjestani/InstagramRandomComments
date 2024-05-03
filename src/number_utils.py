import random
from typing import List


def get_random_numbers(min_val: int, max_val: int, count: int) -> List[int]:
    """
    Generate a list of random numbers within a specified range.

    Parameters:
    - min_val (int): The minimum value of the range.
    - max_val (int): The maximum value of the range.
    - count (int): The number of random numbers to generate.

    Returns:
    - List[int]: A list of randomly selected numbers within the specified range.

    Raises:
    - ValueError: If the count is greater than the difference between min_val and max_val, or if min_val is greater than max_val.
    """
    if count > max_val - min_val:
        raise ValueError("Count is greater than the difference between min and max")
    if min_val > max_val:
        raise ValueError("Min is greater than max")

    return random.sample(range(min_val, max_val), count)
