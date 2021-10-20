"""List utility functions."""

__author__ = "730395502"


def all(xs: list[int], x: int) -> bool:
    """Indicates whether or not all ints in the list are the same as the given int."""
    


def is_equal(xs: list[int], ys: list[int]) -> bool:
    """Tests if every element at every index is equal in both lists."""



def max(input: list[int]) -> int:
    """Determines the max value of a list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        max = input[0]
        for item in input:
            if item > max:
                max = item
        return(max)


def main() -> None:
    """Tests functions calls."""
    print(all([1, 2, 2], 1))
    print(is_equal([2, 3, 1], [1, 2, 3]))
    print(max([100, 99, 98]))


if __name__ == "__main__":
    main()