from enum import Enum


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

number = "20"

age = int(number)
print(isinstance(age, int))

x = 8
x *= 8
print(x)

print(0 or 1)
print(False or "hey")
print("hi" or "hey")

print(["kl"] or False)
print([] or False)


def is_adult(age):
    if age > 18:
        return True
    else:
        False


v = is_adult(20)
print(v)


def is_adult2(age):
    return True if age > 18 else False


r = is_adult2(10)
print(r)

"Beau"
'Beau'

name = "Beau"
name += " is my name"
print(name)

print("""

Hi 


it's 


me

""")


print("leopard".upper())
print("LEOPARD".lower())
print("LeOpArD".title())

print("leopard".upper())
print("LEOPARD".lower())
print("LeOpArD".title())

print("leopard".isupper())
print("leopard".islower())
print("leopard".istitle())


name = "Bapu"
print("apu " in name)
print("apu" in name)
print("apun" in name)


name = "Jack"
print(name[0])
print(name[1])
print(name[2])
print(name[3])

print(name[-1])
print(name[-2])
print(name[-3])
print(name[-3])
print(name[-4])

name = "Jack is cool"
print(name[1:4])

print(round(3.4))


class State(Enum):
    ACTIVE = 1
    INACTIVE = 0


print(list(State))
print(len(State))

age = input("Enter your age: ")
print("I am "+age+" years old.")
