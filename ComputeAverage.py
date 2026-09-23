# Program Name: Compute Average
# File Name: ComputeAverage.py
# Author: Trevor M. Tomesh
# Course: CIDS 161
# Date: Sept. 21st 2026
# Assignment #1

# Description:
# This program asks the user for three numbers and computes the average
# and tells the user the average.

# Prompt the user for three numbers.
number_1 = eval(input("Enter the first number: "))
number_2 = eval(input("Enter the second number: "))
number_3 = eval(input("Enter the third number: "))
number_4 = eval(input("Enter the fourth number: "))

# Compute average
average = (number_1 + number_2 + number_3 + number_4)/4

# Display result
print("The average of",number_1,number_2,number_3, number_4, "is",int(average))

