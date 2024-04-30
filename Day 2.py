#Data Types

# Write a program that adds in a two digit number
#
# two_digit_number = input("Enter two digit number: ")
# num_1 = int(two_digit_number[0])
# num_2 = int(two_digit_number[1])
# answer = num_1 + num_2
# print(answer)

# Mathematical Operations
#order of arrangement when dealing with mathematical operators
#PEMDAS (() ** * / + -)
#print(3 * 3 + 3 / 3 - 3)
#print(3 * (3 + 3) / 3 - 3)

#BMI Calculator Project


# height = input("Enter your height in m:\n ")
# weight = input("Enter your weight in kg:\n ")
# new_weight = int(weight)
# new_height = float(height)
# bmi = new_weight / new_height**2
# bmi_as_int = int(bmi)
# print(bmi_as_int)

# LIFE IN WEEKS PROJECT

# age = input("what is your age? \n")
# age_int = int(age)
# years_left = 90 - age_int
# 1
# days_left = years_left * 365
# weeks_left = years_left * 52
# months_left = years_left * 12
#
# message = f"you have {days_left} days, {weeks_left} weeks and {months_left} months left"
# print(message)

# TIP CALCULATOR

print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? \n"))
split_bill = int(input("How many people to split the bill?\n"))
bill_with_tip= percentage / 100 * bill + bill
split_ways = bill_with_tip / split_bill
#converting to two decimal places
split_in_2dp = "{:.2f}".format(split_ways)
print(f"Each person should pay: ${split_in_2dp}")





