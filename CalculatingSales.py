# CalculatingPlants.py - a basic plant cost calculator

# Ask the user how many pizzas they want, get the number with eval()
number_of_plants = eval(input("How many plants do you want"))

# Ask for the menu cost of each pizza
cost_per_plant = eval(input("How much does each plant cost?"))

# Calculate the total cost of the plants as our subtotal
subtotal = number_of_plants * cost_per_plant

# Calculate the sales tax owed, at 8% of the subtotal
tax_rate = 0.0625  # NJ sales tax at 6.25% as the decimal value
sales_tax = subtotal * tax_rate

# Add the sales tax to the subtotal for the final total
total = subtotal + sales_tax

# Show the user the total amount due, including tax
print("The total cost is $", total)
print("This includes $", subtotal, "for the plant and")
print("$", sales_tax, "in sales tax.")
