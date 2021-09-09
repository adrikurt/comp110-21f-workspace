"""Counting letters in a string."""

__author__ = "730395502"



letter: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")
index_value = 0 
count = 0 
while(index_value < len(word)):
    if (word[index_value] == letter):
        count += 1
    index_value += 1
print("Count: " + str(count))
