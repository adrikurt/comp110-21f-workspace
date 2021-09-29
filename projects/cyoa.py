"""Choose Your Own Adventure Project."""

__author__ = "730395502"

player: str = ""
points: int = 0
pet: str = ""
DOG: str = "\U0001F436"
CAT: str = "\U0001F431"
FROG: str = "\U0001F438"
BONE: str = "\U0001F9B4"
FISH: str = "\U0001F41F"
FLY: str = "\U0001FAB0"
CANDY: str = "\U0001F36D"
ALIEN: str = "\U0001F47E"
BUBBLE_TEA: str = "\U0001F9CB"


def greet() -> None:
    """Greeting to the player."""
    global player
    player = input("What is your name? ")
    print(f"Hello {player}, welcome to the animal shelter game.")
    print("In this game you will choose an animal you want to adopt and take care of it.")


def choose(choice: str) -> str:
    """Allows player to pick which pet they want."""
    int_choice = int(choice)
    if int_choice == 1:
        global pet
        pet = DOG
    else:
        if int_choice == 2:
            pet = CAT
        else:
            pet = FROG
    global points
    points += 1
    return(pet)
    

def name() -> None:
    """Player can name their pet."""
    print(f"{player}, you will now choose a name for your pet.")
    pet_name: str = input("What would you like to name your pet? ")
    print(f"{pet_name} is a great choice. Well done!")
    global points
    points += 1


def feed(food: int) -> int:
    """Allows player to feed their pet."""
    parameter: int = 0
    if food == 1:
        global pet
        if pet == DOG:
            print(f"{pet} + {BONE}")
        else:
            if pet == CAT:
                print(f"{pet} + {FISH}")
            else:
                print(f"{pet} + {FLY}")
        parameter = 1
        print(f"{player}, this is healthy for your pet. Yumm Yumm!")
    else:
        from random import randint
        number: int = randint(1, 3)
        if number == 1:
            print(f"{pet} + {CANDY}")
        else:
            if number == 2: 
                print(f"{pet} + {ALIEN}")
            else:
                print(f"{pet} + {BUBBLE_TEA}")
        parameter = -1
        print(f"{player}, this food was not good for your pet. It has a stomach ache.")
    return(parameter)


def main() -> None: 
    """The program's entrypoint."""
    global points
    points += 1
    greet()
    choose(input("Type the number corresponding to the pet you want to choose. 1.Dog    2.Cat   3.Frog "))
    global pet
    print(pet)
    print("You have three options to proceed. Please type the number corresponding to the option you want to pick.")
    path: str = input("1.End Game   2.Name Pet   3.Feed Pet ")
    int_path = int(path)
    while int_path > 1:
        if int_path == 2:
            name()
            print(f"You have accumulated {points} points. Good job!")
            print("You have three options to proceed. Please type the number corresponding to the option you want to pick.")
            path = input("1.End Game   2.Name Pet   3.Feed Pet ")
            int_path = int(path)
        else:
            print("You can now feed your pet. You will gain or loose points based on whether the food is appropriate for the type of animal your pet is.")
            print("Type the number corresponding to the option you want to choose.")
            food_path: str = input("1.Feed your pet a typical food. 2.Feed your pet a random food. ")
            int_food_path = int(food_path)
            points = feed(int_food_path) + points
            print(f"You have accumulated {points} points. Good job!")
            print("You have three options to proceed. Please type the number corresponding to the option you want to pick.")
            path = input("1.End Game   2.Name Pet   3.Feed Pet ")
            int_path = int(path)
    else:
        print(f"{player}, thank you for playing the animal shelter game.")
    print(f"You have accumulated {points} points. Good job!")


if __name__ == "__main__":
    main()