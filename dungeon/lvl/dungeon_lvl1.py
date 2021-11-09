import random

# define situation and first question
Situation_01 = ("You are in a building and have one knife" + ". " + "The murder is in it" + ". " +
                " What do you do? ")
print(Situation_01)


# define function decisions
def decisions():
    print("You're decision is correct" + " .")
    return True


# define options
option_01 = ("a" + ") " + "You kill the murder" + ".")
option_02 = ("b" + ") " + "You run away" + ".")
option_03 = ("c" + ") " + "You wait" + ".")
print(option_01, option_02, option_03)
print("Choose a, b or c" + "! ")

# type in the answer
answer_for_situation_01 = input("Type in your answer: ")

# declare true and false booleans
option_01 = False
option_02 = False
option_03 = True

# sum up options
options = [str(option_01), str(option_02), str(option_03)]

# programming a loop to end when right answer is typed in
for i in options:
    if i is True:
        print("The light in the kitchen is on" + ". " + "He is in the kitchen" + ". "
              + "You climbed through the window, hid behind and killed him" + ".")
else:
    print("Game Over")
