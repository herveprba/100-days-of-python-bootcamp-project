# 💸 Day 2: Tip Calculator

A simple Command-Line Interface (CLI) application that calculates the total bill amount including a custom tip percentage, then splits the final total evenly among a group of people. This project was built on Day 2 of my **100 Days of Code™: The Complete Python Pro Bootcamp** journey.

## 📖 Overview

The program helps users split dinner or service bills without doing mental math by:

1. Requesting the original total bill amount.
2. Asking for the desired tip percentage (e.g., 10%, 12%, or 15%).
3. Prompting for the number of people splitting the bill.
4. Calculating each person's exact share rounded to 2 decimal places.

## 💻 Code Snippet

```python
"""
Tip Calculator
A simple CLI program that calculates the total bill including tip 
and splits the amount evenly among a specified number of people.
"""

# Display welcome banner
print("Welcome to the tip calculator!")

# 1. Collect inputs from the user
bill = float(input("What was the total bill? $"))
tip_percentage = int(
    input("How much tip would you like to give? 10, 12, or 15? ")
)
people = int(input("How many people to split the bill? "))

# 2. Calculate tip amount and total bill
tip_amount = bill * (tip_percentage / 100)
total_bill = bill + tip_amount

# 3. Calculate the split amount per person
amount_per_person = round(total_bill / people, 2)

# 4. Display the result
print(f"Each person should pay: ${amount_per_person}")
```

## 🎯 Example Output

```text
Welcome to the tip calculator!
What was the total bill? $124.56
How much tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 7
Each person should pay: $19.93
```

## 💡 Concepts Learned Today

On Day 2 of the bootcamp, I explored fundamental data handling concepts in Python:

* **Primitive Data Types**: Working with Integers, Floats, Strings, and Booleans.
* **Type Errors & Type Checking**: Identifying data types using `type()` to avoid implicit type mismatch errors.
* **Type Conversion (Casting)**: Converting user input strings into numerical data types like `float()` and `int()`.
* **Mathematical Operations**: Applying arithmetic operators (`+`, `-`, `*`, `/`) and understanding PEMDAS execution order.
* **Number Manipulation**: Rounding floating-point numbers using the `round()` function to limit decimal places.
* **F-Strings**: Injecting variables directly into strings using `f"..."` formatting for clean and readable output.

## 🚀 How to Run

1. Open your terminal or command prompt.
2. Navigate to this project folder:
   ```bash
   cd day-02-tip-calculator
   ```
3. Execute the Python script:
   ```bash
   python main.py
   ```

## 🔙 Navigation

[⬅️ Back to Main Repository](../README.md)