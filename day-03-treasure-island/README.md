# 🏝️ Day 3: Treasure Island

A interactive, text-based CLI adventure game where players make strategic decision choices to navigate through a island full of choices to find hidden treasure. This project was built on Day 3 of my **100 Days of Code™: The Complete Python Pro Bootcamp** journey.

## 📖 Overview

The game guides the player through a branching story tree using user inputs:

1. **Crossroads Decision**: Choose to go `left` or `right`.
2. **Lake Decision**: Choose to `wait` for a boat or `swim` across.
3. **Door Choice**: Choose between a `red`, `yellow`, or `blue` door to find the treasure.

Any wrong decision results in a humorous or sudden "Game Over"!

## 💻 Code Snippet

```python
"""
Treasure Island
A text-based adventure game where strategic choices lead to treasure or game over.
"""

# Display game ASCII art banner
print('''
*******************************************************************************
          |                    |                  |                     |
_________|________________.=""_;=.______________|_____________________|_______
|                    |  ,-"_,=""      `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
_________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                    |    .--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |            |o`"=._` , "` `; .". ,  "-._"-._; ;              |
_________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                    | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')

# Display welcome messages
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# First decision: Choose direction
choice1 = input(
    "You're at a crossroads. Where do you want to go?\n"
    "    Type 'left' or 'right'.\n"
).lower()

if choice1 == "left":
    # Second decision: Wait or swim
    choice2 = input(
        "You've come to a lake. There is an island in the middle of the lake.\n"
        "    Type 'wait' to wait for a boat. Type 'swim' to swim across.\n"
    ).lower()

    if choice2 == "wait":
        # Third decision: Select a door
        choice3 = input(
            "You arrive at the island unharmed. There is a house with 3 doors.\n"
            "    One red, one yellow, and one blue. Which colour do you choose?\n"
        ).lower()

        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure. You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
```

## 🎯 Example Output

```text
Welcome to Treasure Island.
Your mission is to find the treasure.
You're at a crossroads. Where do you want to go?
    Type 'left' or 'right'.
left
You've come to a lake. There is an island in the middle of the lake.
    Type 'wait' to wait for a boat. Type 'swim' to swim across.
wait
You arrive at the island unharmed. There is a house with 3 doors.
    One red, one yellow, and one blue. Which colour do you choose?
yellow
You found the treasure. You Win!
```

## 💡 Concepts Learned Today

On Day 3 of the bootcamp, I mastered logic branching and flow control in Python:

* **Modulo Operator (`%`)**: Checking remainders to determine odd or even numbers.
* **Control Flow (`if / elif / else`)**: Creating multi-branch decision structures to direct code execution based on conditions.
* **Nested Conditionals**: Placing conditional checks inside other conditional blocks to build multi-level branching paths.
* **Logical Operators (`and`, `or`, `not`)**: Combining multiple boolean expressions to build complex condition checks.
* **String Standardization (`.lower()`)**: Converting user inputs to lowercase to prevent casing mismatch errors.

## 🚀 How to Run

1. Open your terminal or command prompt.
2. Navigate to this project folder:
   ```bash
   cd day-03-treasure-island
   ```
3. Execute the Python script:
   ```bash
   python main.py
   ```

## 🔙 Navigation

[⬅️ Back to Main Repository](../README.md)