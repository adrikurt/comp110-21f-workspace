"""List utility functions part 2."""

__author__ = "730395502"


# Define your functions below
def only_evens(original: list[int]) -> list[int]:
    """Returns a list containing only the elements of the input list that were even."""
    even: list[int] = []
    for item in original:
        if item % 2 == 0:
            even.append(item)
    return even


def sub(original: list[int], start: int, end: int) -> list[int]:
    """Generates a list which is a subset of the given list, between the specifed start index and the end index -1."""
    sublist: list[int] = []
    for index in original: 
        while len(original) >= start and len(original) < end:
            sublist.append(index)
    return sublist


def concat(x: list[int], y: list[int]) -> list[int]:
    """Generates a new list composed of all of the elements of the first list followed by all of the elements of the second list."""
    for item in y:
        x.append(item)
    return x