# Control flow with if/else
# number = int(input("What number would you like to check?\n "))
#
# if number % 2 == 0:
#     print("This number is an even number")
# else:
#     print("This number is an odd number")

# BMI Calculator 2.0
#
# height = float(input("What is your height in m: \n"))
# weight = float(input("What is your weight in kg: \n"))
# bmi = round(weight / (height ** 2))
# print(bmi)
# if bmi < 18.5:
#     print(f"Your BMI is {round(bmi)} , and you are underweight. ")
# elif bmi < 25:
#     print(f"Your BMI is {round(bmi)} , and you are normal weight. ")
# elif bmi < 30:
#     print(f"Your BMI is {round(bmi)} , and you are over weight. ")
# elif bmi < 35:
#     print(f"Your BMI is {round(bmi)} , and you are obese. ")
# else:
#     print(f"Your BMI is {round(bmi)} , and you are clinically obese! "
#           f", You could die soon ")

# Leap Year Calculator

#   year = int(input("Which year do you want to check? "))
# if year % 4 == 0:
#     if year % 100 != 0:
#         print("It is a leap year.")
#     elif year % 400 == 0:
#         print("It is a leap year.")
# else:
#     print ("it is not a leap year")
#
# Pizza Order Project

# print("Welcome to Python Pizza Deliveries")
# size = (input("What size of pizza do you want? S, M, or L "))
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# bill = 0
# if size == "S":
#     bill += 15
# if size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
# if extra_cheese == "Y":
#     bill += 1
# print(f"Your final bill is ${bill}")


# Love Calcuulator
# print("Welcome to love calculator")
# name_1 = input("what is your name? \n")
# name_2 = input("what is their name? \n")
#
# name_3 = name_1 + name_2
# lower_case_string = name_3.lower()
# t = lower_case_string. count("t")
# r = lower_case_string . count("r")
# u = lower_case_string.count("u")
# e = lower_case_string .count("e")
# true = str(t + r + u + e)
# l = lower_case_string.count("l")
# o = lower_case_string.count("o")
# v = lower_case_string.count("v")
# x = lower_case_string.count("e")
# love = str(l + o + v + x)
# score = int(true + love)
# if score < 10 or score > 90:
#     print(f"Your score is {score}% , you go together like coke and mentos.")
# elif 40 <= score <= 50:
#     print(f"Your score is {score}% , you are alright together")
# else:
#     print(f"Your score is {score}%")

# Treasure Island
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
left_or_right = input("You are at a cross road where do you want to go? Type (left) or (right):\n")
left_or_right = left_or_right.lower()
if left_or_right == "left":
    wait_swin = input(";-) Ok you passed my first obstacle , well now you come to a lake. There is an island is "
                      "the middle of the lake. Type (wait) to wait for a boat. Type (swin) to  swin across:\n")
    wait_swin = wait_swin.lower()
    if wait_swin.lower() == "wait":
        house_colour = input("You arrive at three different house 1. Yellow 2. Green 3. Red. Pick a number to select a "
                             "house colour:\n")
        house_colour = house_colour.lower()
        if house_colour == "2":
            print("Congratulations! You are the owner of a brand new house in the Hampton's :-}")
        elif house_colour == "1":
            print("Opps you just missed out on a house in the Hampton's")
        elif house_colour == "3":
            print("Opps you just missed out on a house in the Hampton's")
        else:
            print("That door doesnt exist")
    else:
        print("Opps you were eaten by crocs  :-|")
else:
    print("hahah Opps you chose wrong. Game Over :-o")
