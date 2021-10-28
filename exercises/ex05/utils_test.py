"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730395502"


def test_only_evens_empty() -> None:
    """Tests an empty list."""
    original: list[int] = []
    assert only_evens(original) == []


def test_only_evens_one_odd() -> None:
    """Tests list with one odd number and the rest even numbers."""
    original: list[int] = [1, 2, 4, 6]
    assert only_evens(original) == [2, 4, 6]


def test_only_evens_evens() -> None:
    """Tests list with only even numbers."""
    original: list[int] = [2, 4, 6, 8]
    assert only_evens(original) == [2, 4, 6, 8]


def test_sub_empty_list() -> None:
    """Tests an empty list."""
    original: list[int] = []
    start: int = 1
    end: int = 2
    assert sub(original) == []


def test_sub_negative_index() -> None:
    """Tests negative starting index."""
    original: list[int] = [1, 2, 3, 4, 5, 6]
    start: int = -1
    end: int = 2
    assert sub(original) == [1, 2, 3]


def test_sub_large_end_index() -> None:
    """Tests ending index that is larger than the length of the list."""
    original: list[int] = [1, 2, 3, 4]
    start: int = 0
    end: int = 4
    assert sub(original) == [1, 2, 3, 4]


def test_concat_both_empty() -> None:
    """Tests both lists being empty."""
    x: list[int] = []
    y: list[int] = []
    assert concat(x) == []


def test_concat_one_empty() -> None:
    """Tests one list being empty."""
    x: list[int] = [1, 2]
    y: list[int] = []
    assert concat(x) == [1, 2]
