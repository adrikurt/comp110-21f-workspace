"""Program to practice the numerical operators, type conversions, and string concatenation."""

__author__ = "730395502"

left_hand_side: str = input("Left-hand side: ")
right_hand_side: str = input("Right-hand side: ")
int_left_hand_side = int(left_hand_side)
int_right_hand_side = int(right_hand_side)
print(left_hand_side + " ** " + right_hand_side + " is " + str (int_left_hand_side ** int_right_hand_side))
print(left_hand_side + " / " + right_hand_side + " is " + str (int_left_hand_side / int_right_hand_side))
print(left_hand_side + " // " + right_hand_side + " is " + str (int_left_hand_side // int_right_hand_side))
print(left_hand_side + " % " + right_hand_side + " is " + str (int_left_hand_side % int_right_hand_side))