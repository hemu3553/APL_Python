'''
  * Python Programming for Data Scientists and Engineers
  * LAB #3-1 Convert each character into a list or tuple
  * #11 Chia-Hui Amy Lin
'''

# Prompt user for a sentence or a word
usersMind = input("Please enter what's in your mind : ")

# Take out spaces in user's input.
# Assume other symbols besides empty space is
usersMind = map(lambda x: x.strip(' '), usersMind)
usersMind = " ".join(usersMind).split()

# Break down into characters in a List
list_type = list(usersMind)
# Break down into characters in a Tuple
tuple_type = tuple(usersMind)

# Output results in both formats
print("------------------------------------------------------------")
print("<< List Format >>")
print(list_type)
print("------------------------------------------------------------")
print("<< Tuple Format >>")
print(tuple_type)
print("------------------------------------------------------------")
