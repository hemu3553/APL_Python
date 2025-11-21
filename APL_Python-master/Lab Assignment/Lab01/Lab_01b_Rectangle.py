'''
  * Python Programming for Data Scientists and Engineers
  * LAB #1-b Use length and breadth from user to calculate perimeter.
  * Assume Only Takes Integers.
  * #11 Chia-Hui Amy Lin
'''

# Prompt user for 2 numbers - length and width.
# Ask for another prompt if either of them is an invalid input.
flag = False
while True:
    user_length = input("Please enter a number for LENGTH : ")
    try:
        iuser_length = int(user_length)
    except ValueError or TypeError:
        print("Invalid input. Please enter an INTEGER." + "\n")
        flag = True
    else:
        flag2 = False
        while True:
            user_width = input("Please enter a number for WIDTH : ")
            try:
                iuser_width = int(user_width)

            except ValueError or TypeError:
                print("Invalid input. Please enter an INTEGER." + "\n")
                flag2 = True
            else:
                break
        break

# Calculate the perimeter for the ractangle
rectangle_perimeter = iuser_length * 2 + iuser_width * 2

# Output the result
print("=========================================================================")
print("Perimeter of the triangle with length " + user_length + " and " + user_width + " is " + str(rectangle_perimeter))
print("=========================================================================")
