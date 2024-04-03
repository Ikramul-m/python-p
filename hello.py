import random


def get_choice():
    player_choice = input("Enter a choice (rock, paper, sicors): ")
    computer_choice = "paper"
    choices = {"player": player_choice, "computer": computer_choice}

    return choices


choice = get_choice()
print(choice)

food = ["pizza", "burger", "eggs"]
dinner = random.choice(food)
print(dinner)

