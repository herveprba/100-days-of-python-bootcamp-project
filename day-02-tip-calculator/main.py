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