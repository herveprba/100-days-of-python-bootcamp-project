"""
Password Generator
A CLI program that generates a randomized, secure password based on 
user preferences for letters, symbols, and numbers.
"""

import random

# Define character sets
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '_',
           '=', '+', '[', ']', '{', '}', ';', ':', '.', ',', '?', '/']

print("Welcome to the Password Generator!")

# 1. Collect user preferences
total_number_of_letters = int(input("How may letters would you like in your password?\n"))
total_number_of_symbols = int(input("How many symbols would you like?\n"))
total_number_of_numbers = int(input("How many numbers would you like?\n"))

password_list = []

# 2. Add random characters based on specified counts
for i in range(0, total_number_of_letters):
    password_list.append(random.choice(letters))

for i in range(0, total_number_of_symbols):
    password_list.append(random.choice(symbols))

for i in range(0, total_number_of_numbers):
    password_list.append(random.choice(numbers))

# 3. Shuffle list to randomize character order
random.shuffle(password_list)

# 4. Convert list to a single string
password = ""
for char in password_list:
    password += char

# 5. Display the generated password
print(f"Your password is: {password}")