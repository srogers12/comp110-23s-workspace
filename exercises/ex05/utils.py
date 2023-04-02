"""Exercise 5."""

__author__ = "730466526"


def only_evens(a: list[int]) -> list[int]:
    """Provide a list of the even numbers in the list."""
    new_list: list[int] = []
    for number in a:
        if number % 2 == 0:
            new_list.append(number)
    return new_list


def concat(list_one: list[int], list_two: list[int]):
    """Combine both list into one."""
    new_list: list[int] = []
    for number in list_one:
        new_list.append(number)
    for number in list_two:
        new_list.append(number)
    return new_list


def sub(list_three: list[int], start: int, end: int) -> list[int]:
    """Given a list and index, provide numbers between the index."""
    new_list: list[int] = []
    if list_three == [] or start >= end:
        return []
    if start < 0:
        start = 0
    if end > len(list_three):
        end = len(list_three)
    for number in range(start, end):
        new_list.append(list_three[number])
    return new_list
