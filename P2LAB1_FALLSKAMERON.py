#Kameron Falls
#10/2/2024
#P2LAB1
#Using Imported library, math and f-string
#Import math library
import math

#get radius from user
radius = float(input("What is the radius of the circle? "))

#calculate diameter
diameter = 2 * radius

#display diameter with one decimal please
print(f"The diameter of the circle is {diameter:.1f}\n")

#calculate circumference
CFE = 2 * math.pi * radius

#display circumference with two decimal place
print(f"The Circumference of the circle is {CFE:.2f}\n")

#Calculate area
area = math.pi * radius **2

#display area with two decimal place
print(f"The area of the circle is {area:.3f}\n")
