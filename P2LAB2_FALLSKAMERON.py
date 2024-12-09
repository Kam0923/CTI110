# Kameron Falls
# 10/2/2024
# P2LAB2
# using dictionaries
#create dictionary
cars_mpg = {"Camaro":18.21, "Prius":52.36, "Model S":110, "Silverado":26}
print()
#Print all keys in dictionary
print(cars_mpg.keys())
print()
#Get a car (key) from the user
userCar = input("Enter a vehicle to see it's mpg: ")
print()
#Display mpg for user car
print(f"The {userCar} gets {cars_mpg[userCar]} mpg.")
print()
#Get miles to drive from user
miles_to_drive = float(input(f"How many miles would you like to drive the {userCar}? "))
print()

#Calculate gallons of gas needed
gallons_needed = miles_to_drive/cars_mpg[userCar]
#Display gallons of gas needed
print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {userCar} {miles_to_drive} miles. ")
