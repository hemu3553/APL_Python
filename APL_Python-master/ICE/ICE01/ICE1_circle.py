'''
  * Python Programming for Data Scientists and Engineers
  * ICE #1-2-b
  * Take radius of a circle as input from user.
  * Calculate area, circumference and print the output.
  * #11 Chia-Hui Amy Lin
'''

# Libraries import
import math

# Prompt user input of the radius of the circle
user_radius = float(input("Please enter the radius of the circle : "))

# Calculate area and circumference
area = math.pi * user_radius * user_radius  # pi * r * r
circumference = 2 * math.pi * user_radius   # 2 * pi * r

# Output the calculations
print("\n" + "Calculation Output :")
print("-----------------------------------------------------")
print("Area = ", area)
print("Circumference = ", circumference)
print("-----------------------------------------------------")
