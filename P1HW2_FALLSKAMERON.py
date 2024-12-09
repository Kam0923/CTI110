# Kameron Falls
# Date
# P1HW2
# Create budget for vacation
print("Welcome to your friendly budjet tool! \n")
# Ask user to enter budget and location
budget = float(input("Enter Budget: "))
print()
destination = input("Enter your travel destination: ")
print()
# Ask user for expenses
fuel_cost = float(input("How much do you think you will spend on gas? "))
print()
accommodation_cost = float(input("Approximately, how much will you need for accommodation/hotel? "))
print()
food_cost = float(input("Lastly, how much will you need for food? "))
# Calculate the balance after expenses
total_expenses = fuel_cost + accommodation_cost + food_cost
remaining_balance = budget - total_expenses
print()
print("\n------------Travel Expenses------------")
print(f"Location: {destination}")
print(f"Initial Budget: {budget}")
print()
print(f"Fuel: {fuel_cost}")
print(f"Accommodation: {accommodation_cost}")
print(f"Food: {food_cost}")
print(f"Remaining Balance: {remaining_balance}")
