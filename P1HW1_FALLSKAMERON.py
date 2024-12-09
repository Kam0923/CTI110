# Falls
# 9/18/2024
# P1HW1
# Using math expressions with user input
print("-------Calculating Exponents-------")
print()
print()
#Get input from user
base_value = input("Enter an integer as the base value: ")
print()
# Convert base_value to integer
base_value = int(base_value)
# Get input from user and convert to integer
exponent = int(input("Enter an integer as the exponent: "))
print()
# Display math result to user
print(base_value, "raised to the power of", exponent, "is", str(base_value**exponent) + "!!!")
print()
print("-------Addition and Subtraction-------")
print()
print()
# Get integers from user
 
start_num = int(input("Enter a starting integer: "))
add_num = int(input("Enter an integer to add: "))
sub_num = int(input("Enter an integer to subtract: "))
print()
# Calculate the result
result = start_num = add_num - sub_num
#Display all variables and result
print(start_num, "+", add_num, "-", sub_num, "is equal to", result)
