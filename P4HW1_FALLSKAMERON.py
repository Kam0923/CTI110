#Kameron Falls
#P4HW2
#Payroll breakdown
#11/09/24
#List to hold all employees' payroll data
payroll_data = []
#Loop to input employee data until "Done" is entered
while True:
 #Get employee name
 employee_name = input("Enter employee's name or 'Done' to terminate: ")
 if employee_name.lower() == "done":
 break # Exit loop if user types "Done"

 #Input validation for hours worked and pay rate
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
 #Store employee payroll data in a dictionary
 employee_data = {
 "name": employee_name,
 "hours_worked": hours_worked,
 "pay_rate": pay_rate,
 "overtime_hours": overtime_hours,
 "overtime_pay": overtime_pay,
 "regular_pay": regular_pay,
 "gross_pay": gross_pay
 }
 payroll_data.append(employee_data)
#Display individual employee payroll data
print()
print("PAYROLL SUMMARY")
print("-" * 40)
for data in payroll_data:
 print(f"Employee Name: {data['name']}")
 print("Hours Worked Pay Rate OverTime OverTime Pay RegHour Pay Gross Pay")
 print("-------------------------------------------------------------")
 print(f"{data['hours_worked']:<13.1f}{data['pay_rate']:<10.2f}{data['overtime_hours']:<10.1f}${data['overtime_pay']:<13.2f}${data[
'regular_pay']:<11.2f}${data['gross_pay']:<10.2f}")
 print("-" * 40)
#Calculate totals
total_employees = len(payroll_data)
total_overtime_pay = sum(data["overtime_pay"] for data in payroll_data)
total_regular_pay = sum(data["regular_pay"] for data in payroll_data)
total_gross_pay = sum(data["gross_pay"] for data in payroll_data)
#Display overall summary
print()
print("OVERALL PAYROLL TOTALS")
print("-" * 40)
print(f"Total number of employees entered: {total_employees}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
print("-" * 40)
