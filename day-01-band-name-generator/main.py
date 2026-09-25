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