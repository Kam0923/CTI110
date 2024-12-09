#Kameron Falls
#P3HW1
#10/25/24
# Get user input
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))
# Regular hours threshold
regular_hours = 40
overtime_rate = 1.5
# Calculate overtime and regular pay
if hours_worked > regular_hours:
 overtime_hours = hours_worked - regular_hours
 regular_pay = regular_hours * pay_rate
 overtime_pay = overtime_hours * pay_rate * overtime_rate
else:
 overtime_hours = 0
 regular_pay = hours_worked * pay_rate
 overtime_pay = 0
# Calculate gross pay
gross_pay = regular_pay + overtime_pay
# Print the results
print("-" * 37)
print(f"{'Employee name:':<15} {employee_name}")
print()
print(f"{'Hours Worked':<15} {'Pay Rate':<10} {'OverTime':<10} {'OverTime Pay':<15} {'RegHour Pay':<15} {'Gross Pay':<10}")
print("-" * 90)
print(f"{hours_worked:<15.2f} {pay_rate:<10.2f} {overtime_hours:<10.2f} {overtime_pay:<15.2f} ${regular_pay:<15.2f} ${gross_pay:<10.2f}")
