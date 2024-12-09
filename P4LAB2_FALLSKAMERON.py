#Kameron Falls
#10/30/2024
#P4LAB2
#using loops to make multiplication tables
#create variable to make program run the first time
run_again = "yes"
#while loop to control the entire program
while run_again == "yes":
 #Get input from user
 userNum = int(input("Enter an integer: "))
 print()
 #check if userNum is positive
 if userNum >= 0:
 #Loop to print multiplication
 for num in range(1,13):
 print(f"{userNum} * {num} = {userNum*num}")

 #If userNum is negative, tell the user
 else:
 print("Program does not handle negative numbers. ")

 print()
 run_again = input("Would you like to run the program again (yes/no)? ").lower()
#loop breaks
print("Exiting program...")
