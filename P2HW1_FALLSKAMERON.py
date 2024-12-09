#Kameron Falls
#Date
#P2HW1
#creating a budget
# This program calculates and displays travel expenses
# Get user input for budget and expenses
budget = float(input("Enter Budget: "))
print()
destination = input("Enter your travel destination: ")
print()
fuel = float(input("How much do you think you will spend on gas? "))
print()
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
print()
food = float(input("Last, how much do you need for food? "))
print()
# Calculate remaining balance
remaining_balance = budget - (fuel + accommodation + food)
# Display formatted travel expenses
print("\n------------Travel Expenses------------")
print(f"{'Location:':<18} {destination}")
print(f"{'Initial Budget:':<18} ${budget:,.2f}")
print(f"{'Fuel:':<18} ${fuel:,.2f}")
print(f"{'Accommodation:':<18} ${accommodation:,.2f}")
print(f"{'Food:':<18} ${food:,.2f}")
print("----------------------------------------\n")
print(f"{'Remaining Balance:':<18} ${remaining_balance:,.2f}")
