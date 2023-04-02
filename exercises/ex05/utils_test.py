"""Testing the functions in exercise 5."""

__author__ = "730466526"


from exercises.ex05.utils import only_evens, concat, sub


def test_only_evens_no_numbers() -> None:
    """Seeing if the set us empty."""
    assert only_evens([]) == []


def test_only_evens_containg_all_even() -> None:
    """Seeing if all numbers are even!"""
    assert only_evens([2, 4, 6, 8, 10]) == [2, 4, 6, 8, 10]


def test_only_evens_containg_all_odds() -> None:
    """Seeing if all numbers are odd!"""
    assert only_evens([1, 3, 5, 7, 9]) == []


def test_concat_with_one_number() -> None:
    """A list containg only one number!"""
    assert concat([4], []) == [4]


def test_concat_same_size() -> None:
    """Combining lists of the same size."""
    assert concat([2, 4], [1, 3]) == [2, 4, 1, 3]


def test_concat_different_size() -> None:
    """Combining lists of different sizes!"""
    assert concat([1, 2, 3], [3, 2]) == [1, 2, 3, 3, 2]


def test_sub_empty() -> None:
    """Seeing if the list is empty"""
    assert sub([], 1, 2) == []


def test_sub_start_bigger_than_end() -> None:
    """Seeing the reutrn value of a set with a start bigger than the end"""
    assert sub([2, 4, 6], 4, 1) == []


def test_sub_one() -> None:
    """Seeing the reutrn value of a set with only one number"""
    assert sub([5], 1, 2) == [5]