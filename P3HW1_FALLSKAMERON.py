#P3HW1
#Falls Kameron
#10/19/24
# This program takes a number grade , determines average and displays letter grade for average.
# Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))
# add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
#determine lowest, highest , sum and average for grades
low = min(grades)
high = max(grades)
total_sum = sum(grades)
avg = total_sum / len(grades)
print()
# Display results
print("\n------------Results------------")
print(f'{"Lowest Grade:":<20}{low:>10.1f}')
print(f'{"Highest Grade:":<20}{high:>10.1f}')
print(f'{"Sum of Grades:":<20}{total_sum:>10.1f}')
print(f'{"Average:":<20}{avg:>10.2f}')
print("--------------------------------")
# determine letter grade for average
if avg >= 90:
 print('Your grade is: A')
else:
 if avg >= 80:
 print('Your grade is: B')
 else:
 if avg >= 70:
 print('Your grade is: C')
 else:
 if avg >= 60:
 print('Your grade is: D')
 else:
 print('Your grade is: F')
