print("Math Calculator")

# Ask the user to enter a math problem
problem = input("Enter a math problem, or 'q' to quit: ")

# Keep going until the user enters 'q' or quit
while (problem != "q"):
    # show the problem, and the answer using eval()
    print("the answer is", problem, "is", eval(problem))
    # Ask for another math problem
    problem = input("Enter another math problem, or 'q' to quit: ")
    # This while loop will keep going until you enter 'q' to quit
