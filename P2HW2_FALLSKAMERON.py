#Kameron Falls
#10/9/2024
#P2HW2
#Simple Grade Calculation Program
#Get grades for 6 modules individually
grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))
#Create a list of all the grades
grades = [grade1, grade2, grade3, grade4, grade5, grade6]
#Calculate the lowest, highest, sum, and average of the grades
lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)
#Display the results
print("\n------------Results------------")
print(f"Lowest Grade: {lowest_grade:.1f}")
print(f"Highest Grade: {highest_grade:.1f}")
print(f"Sum of Grades: {sum_of_grades:.1f}")
print(f"Average: {average_grade:.2f}")
print("--------------------------------")
