# Kameron Falls
#P5Lab
#11/17/24
import random
def math_quiz():
 print("Welcome to Math Quiz")
 while True:
 # Display menu
 print("\nMAIN MENU")
 print("1. Adding Random Numbers")
 print("2. Subtracting Random Numbers")
 print("3. Exit")

 choice = input("Please choose one of the menu options: ")
 if choice == "1":
 play_quiz("+")
 elif choice == "2":
 play_quiz("-")
 elif choice == "3":
 print("Thank you for playing... Bye!!")
 break
 else:
 print("Invalid choice. Please enter 1, 2, or 3.")
def play_quiz(operation):
 # Generate random numbers
 num1, num2 = random.randint(1, 100), random.randint(1, 100)
 # Ensure num1 is larger for subtraction
 if operation == "-" and num1 < num2:
 num1, num2 = num2, num1
 # Calculate correct answer
 correct_answer = num1 + num2 if operation == "+" else num1 - num2
 guesses = 0
 # Display problem
 print(f"\n {num1}")
 print(f"{operation} {num2}")
 # Loop until the user gets the correct answer
 while True:
 try:
 guess = int(input("Enter answer: "))
 guesses += 1
 if guess < correct_answer:
 print("Sorry, guess is too low.")
 elif guess > correct_answer:
 print("Sorry, guess is too high.")
 else:
 print("Congratulations!!!! Your answer is correct.")
 print(f"Number of guesses: {guesses}")
 break
 except ValueError:
 print("Invalid input. Please enter a number.")
