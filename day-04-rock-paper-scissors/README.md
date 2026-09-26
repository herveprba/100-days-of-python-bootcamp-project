# ✂️ Day 4: Rock Paper Scissors

A CLI-based Rock Paper Scissors game featuring ASCII art graphics where players compete against a random computer choice. This project was built on Day 4 of my **100 Days of Code™: The Complete Python Pro Bootcamp** journey.

## 📖 Overview

The game allows the player to challenge the computer in a classic game of Rock, Paper, Scissors:

1. **User Selection**: Choose `0` for Rock, `1` for Paper, or `2` for Scissors.
2. **Input Validation**: Rejects invalid numbers with a custom message.
3. **Computer Opponent**: Randomly selects a move using Python's `random` module.
4. **Visual Display**: Renders ASCII art for both the user's and computer's choices.
5. **Outcome Evaluation**: Determines the winner, loser, or a draw based on standard rules.

## 💻 Code Snippet

```python
"""
Rock Paper Scissors
A CLI-based Rock Paper Scissors game featuring ASCII art graphics.
"""

import random

# ASCII Art graphics
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'    ____)____
           ______)
        __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissors]

# 1. Collect user choice
user_choice = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"
    )
)

# 2. Validate input and run game logic
if user_choice < 0 or user_choice >= 3:
    print("You typed an invalid number. You lose!")
else:
    # Display user choice
    print(f"You chose:\n{game_images[user_choice]}")

    # 3. Generate computer choice
    computer_choice = random.randint(0, 2)
    print(f"Computer chose:\n{game_images[computer_choice]}")

    # 4. Determine the winner
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (
        (user_choice == 0 and computer_choice == 2)
        or (user_choice == 1 and computer_choice == 0)
        or (user_choice == 2 and computer_choice == 1)
    ):
        print("You win!")
    else:
        print("You lose!")
```

## 🎯 Example Output

```text
What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.
0
You chose:

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

Computer chose:

    _______
---'    ____)____
           ______)
        __________)
      (____)
---.__(___)

You win!
```

## 💡 Concepts Learned Today

On Day 4 of the bootcamp, I explored data collections and randomization in Python:

* **Python Modules**: Understanding how to import external and built-in modules (`import random`).
* **Randomization (`random.randint()`)**: Generating random integers to simulate decision-making.
* **Python Lists**: Creating, indexing, updating, appending, and deleting elements in ordered sequences.
* **Index Error Handling**: Understanding zero-based indexing and preventing `IndexError: list index out of range`.
* **Nested Lists**: Structure and usage of multi-dimensional lists.
* **Input Validation & Logic Checks**: Filtering out illegal inputs early before index retrieval.

## 🚀 How to Run

1. Open your terminal or command prompt.
2. Navigate to this project folder:
   ```bash
   cd day-04-rock-paper-scissors
   ```
3. Execute the Python script:
   ```bash
   python main.py
   ```

## 🔙 Navigation

[⬅️ Back to Main Repository](../README.md)