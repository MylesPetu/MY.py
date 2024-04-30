# fruits = ['apple', 'banana']
# for fruit in fruits:
#     print(fruit + ' Pie')

# #Average height exercise
# student_height = input("Enter a list of student height: ").split()
# for n in range(0, len(student_height)):
#     student_height[n] = int(student_height[n])
# print(student_height)
# total_height = 0
# for i in student_height:
#     total_height += i
# print(total_height)
# number_of_student = 0
# for x in student_height:
#     number_of_student += 1
# average_height = round(total_height / number_of_student)
# print(average_height)

#High Score
# student_scores = input("Enter a list of student scores: ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)
# high_score = 0
# for x in student_scores:
#     if x > high_score:
#         high_score = x
# print(f"The highest score in the class is: {high_score}")

# Sum of all even numbers
# sum_of_even_numbers = 0
# for i in range(0, 101, 2):
#     sum_of_even_numbers += i
# print(sum_of_even_numbers)

#FizzBuzz
# for i in range(1, 101):
#     if i % 5 == 0 and i % 3 == 0:
#         print("FizzBuzz")
#
#     elif i % 3 == 0:
#         print("Fizz")
#
#     elif i % 5 == 0:
#         print("Buzz")
#
#     else:
#         print(i)

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#Easy Level

# password = ""
# for i in range(1, nr_letters + 1):
#     password += random.choice(letters)
# for x in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
# for y in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
# print(password)

#Hard Level

password_list =[]
for i in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
for x in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)
for y in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)
random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(password)
