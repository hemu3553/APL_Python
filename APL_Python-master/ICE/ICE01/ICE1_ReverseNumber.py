'''
  * Python Programming for Data Scientists and Engineers
  * ICE #1-2-a
  * Reverse a number.
  * #11 Chia-Hui Amy Lin
'''

# Prompt user input for a number to reverse, store it as string type
originNumInput = str(input("Please enter a number you want to reverse: "))

# Read the user input number backward to get the reverse number
reverseNum = originNumInput[::-1]

# Output the result
print("----------------------------------------------------------")
print("Original Number from user : " + originNumInput)
print("Reverse Number : " + reverseNum)
print("----------------------------------------------------------")
