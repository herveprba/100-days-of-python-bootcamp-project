# 🎸 Day 1: Band Name Generator

A simple Python console application that generates a unique band name based on the city you grew up in and your pet's name. This project marks the start of my **100 Days of Code™: The Complete Python Pro Bootcamp** journey.

---

## 📖 Overview

The program prompts the user for two simple inputs:
1. The name of the city they grew up in.
2. The name of their pet.

It then concatenates these inputs to produce a custom band name recommendation!

---

## 💻 Code Snippet

```python
"""
Band Name Generator
A simple CLI application that combines a city name and a pet's name
to generate a creative band name.
"""

# Display welcome message
print("Welcome to the Band Name Generator.")

# 1. Collect inputs from the user
city = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")

# 2. Combine inputs using string concatenate to generate the band name
band_name = city + " " + pet

# 3. Display the generated band name
print("Your band name could be " + band_name)
```

---

## 🎯 Example Output

```text
Welcome to the Band Name Generator.
What's the name of the city you grew up in?
Jakarta
What's your pet's name?
Milo
Your band name could be Jakarta Milo
```

---

## 💡 Concepts Learned Today

During Day 1 of the bootcamp, I learned and applied foundational Python programming concepts:

- **Printing to the Console (`print()`)**: Displaying text output for the user.
- **String Manipulation**: Working with strings, using escape characters like `\n` for newlines, and concatenating strings using the `+` operator.
- **Interactive Inputs (`input()`)**: Receiving dynamic input directly from the user through the terminal.
- **Python Variables**: Creating, naming, and assigning string values to variables (`city`, `pet`, `band_name`) for reuse throughout the script.

---

## 🚀 How to Run

1. Open your terminal or command prompt.
2. Navigate to this project folder:
   ```bash
   cd day-01-band-name-generator
   ```
3. Execute the Python script:
   ```bash
   python main.py
   ```

---

## 🔙 Navigation

[⬅️ Back to Main Repository](../README.md)