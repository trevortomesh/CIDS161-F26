# Program Name: Circle Computer
# File Name: area.py
# Author: [redacted]

# Description:
# This program asks the user for their name and a radius
# and calculates the area and returns a result.


# ask user for their name and radius so we can
# provide them with the area in a friendly interface
name = input("What is your name? ")
radius = eval(input("Enter a value for radius: "))

# compute area
if radius > 0:
    area = radius * radius * 3.14159

    # print result in a friendly way
    print("Hello",name, "the area for the circle of radius",radius,"is",area)
else:
    print("Oops! Please enter a positive radius only!")
print("Thank you!")