def get_choice():
    player_choice = "EEE"
    computer_choice = "paper"
    choices = {"player": player_choice, "computer": computer_choice}

    return choices


choice = get_choice()
print(choice)


def check_win(player, computer):
    print(f"You chose {player}, computer choose {computer}")
    if player == "rock" and computer == "paper":
        return "Rock shmashes sissor! You win!"


check_win("rock", "paper")

k = check_win("rock", "paper")

print(k)

d = {"ikram": "is obsessed", "age": "24"}
print(d["age"])

name = "Ikramul"

print(type(name))

print(isinstance(name, int))
