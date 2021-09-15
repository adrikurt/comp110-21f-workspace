"""Drawing forests in a loop."""

__author__ = "730395502"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
depth: str = input("Depth: ")
int_depth = int(depth)
to_print: str = ""
while int_depth >= 1:
    to_print += TREE
    int_depth -= 1
    print(to_print)
    