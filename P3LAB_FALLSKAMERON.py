#Kameron Falls
#P3LAB
#10/25/24
#Get user input
amount = float(input("Enter the amount of money as a float: $"))
#Convert the amount to cents
cents = int(amount * 100)
#Calculate the number of dollars, quarters, dimes, nickels, and pennies
dollars = cents // 100
cents = cents % 100
quarters = cents // 25
cents = cents % 25
dimes = cents // 10
cents = cents % 10
nickels = cents // 5
pennies = cents % 5
#Print the results
if dollars > 0:
 print(dollars, "Dollars")
if quarters > 0:
 print(quarters, "Quarters")
if dimes > 0:
 print(dimes, "Dimes")
if nickels > 0:
 print(nickels, "Nickels")
if pennies > 0:
 print(pennies, "Pennies")
#If there is no change
if dollars == 0 and quarters == 0 and dimes == 0 and nickels == 0 and pennies == 0:
 print("No change")
