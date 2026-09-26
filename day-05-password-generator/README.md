# 🔐 Day 5: PyPassword Generator

A Command-Line Interface (CLI) application that generates strong, randomized passwords based on user-defined preferences for letters, symbols, and numbers. This project was built on Day 5 of my **100 Days of Code™: The Complete Python Pro Bootcamp** journey.

## 📖 Overview

The program helps users build secure passwords through an interactive CLI workflow:

1. **User Preferences**: Asks how many letters, symbols, and numbers the user wants in their password.

2. **Random Character Selection**: Uses `random.choice()` within `for` loops to select random characters from pre-defined lists.

3. **In-Place Shuffling**: Applies `random.shuffle()` to randomize the sequence of characters, preventing predictable character ordering (e.g., preventing all letters from appearing before symbols).

4. **String Concatenation**: Reconstructs the shuffled list items into a final string output.

## 💻 Code Snippet

```python
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
```

## 🎯 Example Output

```text
Welcome to the Password Generator!
How may letters would you like in your password?
4
How many symbols would you like?
2
How many numbers would you like?
2
Your password is: $9kA!2xL
```

## 💡 Concepts Learned Today

On Day 5 of the bootcamp, I explored Python loops and sequence manipulation:

* **For Loops with Sequences (`for item in list`)**: Iterating over elements within collections.

* **For Loops with `range()`**: Executing code blocks a specified number of times using numeric ranges.

* **Mathematical Built-ins (`sum()`, `max()`)**: Aggregating list values and finding maximum items natively.

* **List Shuffling (`random.shuffle()`)**: Modifying sequence orders in-place to increase entropy.

* **String Accumulation**: Re-building formatted string sequences from list items.

## 🚀 How to Run

1. Open your terminal or command prompt.

2. Navigate to this project folder:

   ```bash
   cd day-05-password-generator
   ```

3. Execute the Python script:

   ```bash
   python main.py
   ```

## 🔙 Navigation

[⬅️ Back to Main Repository](../README.md)