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