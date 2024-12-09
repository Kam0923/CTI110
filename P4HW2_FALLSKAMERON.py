#Kameron Falls
#P4HW2
#Payroll breakdown
#11/10/24
#totals
total_employees = 0
total_overtime_pay = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0
#Start loop for each employee
while True:
 #Get employee name or termination command
 employee_name = input("Enter employee's name or 'Done' to terminate: ")
 if employee_name.lower() == "done":
 break # Exit the loop if user enters "Done"

 #Get hours worked and pay rate
 hours_worked = float(input(f"How many hours did {employee_name} work? "))
 pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

 #Calculate overtime and regular hours
 if hours_worked > 40:
 overtime_hours = hours_worked - 40
 regular_hours = 40
 else:
 overtime_hours = 0
 regular_hours = hours_worked

 #Calculate pay
 overtime_pay = overtime_hours * (pay_rate * 1.5)
 regular_pay = regular_hours * pay_rate
 gross_pay = regular_pay + overtime_pay

 #Display employee payroll information
 print("\nEmployee name: ", employee_name)
 print("Hours Worked Pay Rate OverTime OverTime Pay RegHour Pay Gross Pay")
 print("-------------------------------------------------------------")
 print(f"{hours_worked:<13.1f}{pay_rate:<10.2f}{overtime_hours:<10.1f}${overtime_pay:<13.2f}${regular_pay:<11.2f}${gross_pay:<10.2f}")
 print("-------------------------------------------------------------\n")

 #Update totals
 total_employees += 1
 total_overtime_pay += overtime_pay
 total_regular_pay += regular_pay
 total_gross_pay += gross_pay
#Display summary information
print("\nTotal number of employees entered:", total_employees)
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
