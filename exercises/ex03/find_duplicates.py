"""Finding duplicate letters in a word."""

__author__ = "730395502"


word: str = input("Enter a word: ")
i: int = 0
j: int = 0
occurance = 1
while i < len(word) - 1:
    j += 1
    while j < len(word) - 1:
        if word[i] == word[j+1]:
            occurance = occurance + 1
        j += 1
    i += 1
if occurance > 1:
    print("Found duplicate: True")
else:
    print("Found duplicate: False")
