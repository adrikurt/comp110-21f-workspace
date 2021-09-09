"""Counting letters in a string."""

__author__ = "730395502"


letter: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")
i = 0 
count = 0 
while(i < len(word)):
    if (word[i] == letter):
        count += 1
    i += 1
print("Count: " + str(count))