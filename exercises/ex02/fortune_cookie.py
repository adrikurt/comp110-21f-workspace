"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730395502"

print("Your fortune cookie says...")
from random import randint
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