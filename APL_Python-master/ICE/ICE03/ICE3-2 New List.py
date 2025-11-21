'''
  * Python Programming for Data Scientists and Engineers
  * ICE #3-2 Make new list
  * Take in a list of numbers.
  * Make a new list for only the first and last elements.
  * #11 Chia-Hui Amy Lin
'''


# Function for prompting user for numbers, append and return the list
def user_enter_num(count_prompt, user_num_list):

    # Prompt user for a number(integer).
    # If it's an invalid input, prompt user again.

    flag = False
    while True:
        user_prompt = input("Please enter 5 numbers : ")
        try:
            user_prompt = int(user_prompt)
        except ValueError or TypeError:
            print("Invalid input. Please enter an INTEGER." + "\n")
            flag = True
            count_prompt -= 1
        else:
            break
    user_num_list.append(user_prompt)
    return user_num_list


# Pre-set number list
numbers = [4, 5, 6, 7, 8]

# Variables for customized number list
user_number = []
count = 0

# Continue to call function user_enter_num until the user entered 5 numbers
while count < 5:
    user_enter_num(count, user_number)
    count += 1

# Output the first and last number of new list from the original one that the user prompted
print("===================================================================")
print("<< User Prompt Number List >>")
print("The Original User Prompt List : ", user_number)
firstLastNumList = user_number[0::len(user_number)-1]
print("New list containing only first and last element(user prompt) : ", firstLastNumList)

# Output the first and last number of new list from the pre-set number list
print("===================================================================")
print("<< Pre-set Number List >>")
print("Original Number List : ", numbers)
presetNumList = numbers[0::len(numbers)-1]
print("New list containing only first and last element(preset) : ", presetNumList)
