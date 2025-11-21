'''
  * Python Programming for Data Scientists and Engineers
  * LAB #3-2 Ascending Tuples
  * #11 Chia-Hui Amy Lin
'''

# Create a list of tuples
tuple_List = [(1, 6), (1, 7), (4, 5), (2, 2), (1, 3)]

# Sort the tuples in ascending order
sort_tuple_Second = sorted(tuple_List, key=lambda sort_sec: sort_sec[1])

# Output the result
print("-----------------------------------------------------------")
print("Sort Second Element in the Tuple by Ascending Order :")
print(sort_tuple_Second)
print("-----------------------------------------------------------")
