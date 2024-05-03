from number_utils import get_random_numbers
from typing import TypeVar, List

T = TypeVar('T')


def get_random_list_items(input_list: List[T], count: int) -> List[T]:
    """
    Generate a list of random items from the input_list.

    Parameters:
        input_list (List[T]): The list from which random items will be selected.
        count (int): The number of random items to select.

    Returns:
        List[T]: A list containing the randomly selected items from input_list.

    Raises:
        ValueError: If count exceeds the length of the input_list.
    """
    length = len(input_list)
    if count > length:
        raise ValueError("Count is greater than the length of the list")

    random_index_list = get_random_numbers(0, length, count)
    return [input_list[index] for index in random_index_list]
