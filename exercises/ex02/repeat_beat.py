"""Repeating a beat in a loop."""

__author__ = "730395502"


beat: str = input("What beat do you want to repeat? ")
repeat: str = input("How many times do you want to repeat it? ")
int_repeat = int(repeat)
to_print: str = ""
if (int_repeat <= 0):
    print("No beat...")
else:    
    while int_repeat > 0:
        if (int_repeat == 0):
            to_print += beat
        else:
            to_print += beat + " "
            int_repeat -= 1
    print(to_print)

