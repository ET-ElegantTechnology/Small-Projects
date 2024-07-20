# HundredNames.py - prints a screen full of the user's name

# Ask the user for their name
name = input("What is your name?")

# Print their name 100 times
for x in range(100):
    print(name, end = " ")  # Print their name followed by a space, not a new line
