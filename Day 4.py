# import random
# # Heads and tails
# random_number = random.randint(0, 1)
# print(random_number)
# if random_number == 0:
#     print("Tails")
# elif random_number == 1:
#     print("Heads")
from random import random

#Lists

# friends_list = ["James", "Bob", "Jane", "Luke", "Specter"]
# print(friends_list[-2])
# friends_list.remove("Specter")
# friends_list.append("Jane")
#
# import random
# #Banker Roulette Who will pay the bill
# names_string = input("Give me everybody's names, seperated by a comma. ")
# names = names_string.split(",")
# print(names)
# randomize_names = random.randint(0, len(names) - 1)
# person_who_will_pay = names[randomize_names]
# print(person_who_will_pay + " is paying for lunch")

# Treasure Map
# row1 = ["😙", "🥸", "🥸"]
# row2 = ["🥸", "🥸", "🥸"]
# row3 = ["🥸", "🥸", "🥸"]
# the_map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("This should be a two digit number signifying row and column in a 3 by 3 matrix "
#                  "Where do you want the treasure to be: ")
#
#
# if position == "11":
#     row1[0] = "X"
# elif position == "12":
#     row1[1] = "X"
# elif position == "13":
#     row1[2] = "X"
# elif position == "21":
#     row2[0] = "X"
# elif position == "22":
#     row2[1] = "X"
# elif position == "23":
#     row2[2] = "X"
# elif position == "31":
#     row3[0] = "X"
# elif position == "32":
#     row3[1] = "X"
# elif position == "33":
#     row3[2] = "X"
# else :
#     print("Invalid entry. Please try again.")
# print(f"{row1}\n{row2}\n{row3}")






# trying out another way
# horizontal = int(position[0])
# vertical = int(position[1])
#
# selected_row =map(vertical-1)
# selected_row[horizontal-1] = "X"

#Projet rock paper scissors
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors:\n "))
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)
else:
    print("Invalid entry. Please try again")
print("Computer choice:")
computer_choice = random.randint(0, 2)
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)

if user_choice == 0 and computer_choice == 0:
    print("Its a Draw")
elif user_choice == 0 and computer_choice == 1:
    print("You lose")
elif user_choice == 0 and computer_choice == 2:
    print("You win")
elif user_choice == 1 and computer_choice == 0:
    print("You win")
elif user_choice == 1 and computer_choice == 1:
    print("Its a Draw")
elif user_choice == 1 and computer_choice == 2:
    print("You win")
elif user_choice == 2 and computer_choice == 0:
    print("You lose")
elif user_choice == 2 and computer_choice == 1:
    print("You win")
elif user_choice == 2 and computer_choice == 2:
    print("Its a Draw")
else:
    print("You have entered an invalid number , You lose")
print("Thank you for playing")


