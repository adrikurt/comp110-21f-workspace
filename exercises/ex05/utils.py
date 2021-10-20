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


def concat(x: list[int], y: list[int]) -> list[int]:
    """Generates a new list composed of all of the elements of the first list followed by all of the elements of the second list."""
    for item in y:
        x.append(item)
    return x