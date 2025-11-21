'''
  * Python Programming for Data Scientists and Engineers
  * LAB #2-1 Print first letter of my name with star.
  * #11 Chia-Hui Amy Lin
'''

# Two dimension array with * that are patterns for each row
pattern = [[" ", "*", "*", "*", " "], [" ", "*", " ", "*", " "], [" ", "*", " ", "*", " "], [" ", "*", "*", "*", " "],
           [" ", "*", " ", "*", " "], [" ", "*", " ", "*", " "], ["*", "*", " ", "*", "*"]]
print("[Pattern for A :]", "\n")
# Go through rows and columns. Print out * in orders to form an " A " pattern
for index in pattern:
    for star in index:
        print(star, end=" ")
    print()
