"""An exercise in remainders and boolean logic."""

__author__ = "730395502"


integer: str = input("Enter an int: ")
int_integer = int(integer)
if (int_integer % 2 == 0 and int_integer % 7 == 0):
    print ("TAR HEELS")
else:
    if (int_integer % 2 == 0):
        print("TAR")
    else:
        if (int_integer % 7 == 0):
            print("HEELS")
        else:
            print("CAROLINA")