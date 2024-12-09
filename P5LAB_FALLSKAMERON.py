#Kameron Falls
#P5LAB
#10/16/24

def calculate_change():
    # Get the total owed and the cash provided
    owed = float(input("You owe: $"))
    cash = float(input("How much cash will you put in the self-checkout? $"))
    
    # Calculate change
    change = round(cash - owed, 2)
    
    if change < 0:
        print("Not enough cash provided.")
        return
    
    print(f"Change is: ${change:.2f}")
    
    # Calculate dollars and coins
    dollars = int(change)
    remaining_cents = round((change - dollars) * 100)
    
    quarters = remaining_cents // 25
    remaining_cents %= 25
    
    dimes = remaining_cents // 10
    remaining_cents %= 10
    
    nickels = remaining_cents // 5
    remaining_cents %= 5
    
    pennies = remaining_cents
    
    # Output change breakdown
    if dollars > 0:
        print(f"{dollars} Dollars")
    if quarters > 0:
        print(f"{quarters} Quarters")
    if dimes > 0:
        print(f"{dimes} Dimes")
    if nickels > 0:
        print(f"{nickels} Nickels")
    if pennies > 0:
        print(f"{pennies} Pennies")

# Example usage
calculate_change()

