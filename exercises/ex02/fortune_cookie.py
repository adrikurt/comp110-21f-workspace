"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730395502"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
#
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100.
from random import randint


print("Your fortune cookie says...")
number: int = randint(1, 4)
if (number == 1):
    print("You will get good grades.")
else:
    if (number == 2):
        print("You will win the lottery.")
    else:
        if (number == 3):
            print("You will get a 4.0 GPA") 
        else:
            print("You will win free food.")       
print("Now, go spread positive vibes!")