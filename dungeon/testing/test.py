
# define situation and first question
from typing import List

lvl1: str = ("You are in a building and have one knife" + ". " + "The murder is in it" + ". ")
print(lvl1)

def options():
option_A: str = ("option_A" + ": " + "You kill the murder" + ".")
print(option_A)
option_B: str = ("option_B" + ": " + "You run away" + ".")
print(option_B)
option_C: str = ("option_C" + ": " + "You wait" + ".")
print(option_C)

# define right and wrong options / correct types / boolean
option_C = str(False)
option_A = str(False)
option_B = str(True)

print("Choose for your life" + "! ")

# type in the answer / output
output_lvl1 = input("Type in your answer: ")

# sum up options
wrong_option = [option_C, option_A]
right_option = [option_B]
options: List[List[str]] = [wrong_option, right_option]

# print out the answer / ending the game for level 1
def answer():
if options == 1:
    print("You survived" + "! ")

