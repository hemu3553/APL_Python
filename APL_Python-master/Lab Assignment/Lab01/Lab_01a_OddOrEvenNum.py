'''
  * Python Programming for Data Scientists and Engineers
  * LAB #1-a Determine the number that user inputs is even or odd.
  * #11 Chia-Hui Amy Lin
'''

# Prompt user for a number(integer).
# If it's an invalid input, prompt user again.
flag = False
while True:
    user_num = input("Please enter an integer number : ")
    try:
        user_num = int(user_num)
    except ValueError or TypeError:
        print("Invalid input. Please enter an INTEGER." + "\n")
        flag = True
    else:
        break

# Number divides by 2 without remainder, it's an Even Num.
# Else, it's an Odd Num.
if(user_num % 2) == 0:
    print("It's an EVEN number!")
elif(user_num % 2) == 1:
    print("That's an ODD number!")
