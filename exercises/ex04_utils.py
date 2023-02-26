"""Practice with Lists."""

__author__ = "730466526"


def all(a: list[int], b: int) -> bool:
    """Indicate whether or not all the ints in the list are the same as the given int."""
    counter: int = 0
    if len(a) == counter:
        return False
    while counter < len(a):
        if a[counter] != b:
            return False
        counter += 1
    return True


def max(input: list[int]) -> int:
    """Returns the largest int in the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an emoty List")
    large = input[0]
    for number in input:
        if number > large:
            large = number
    return large


def is_equal(c: list[int], d: list[int]) -> bool:
    """Indicate whether or not the lists are equal."""
    if c == d:
        return True
    else:
        return False