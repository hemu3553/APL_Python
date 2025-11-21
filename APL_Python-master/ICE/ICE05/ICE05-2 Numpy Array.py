# ------------------------------------------------------------------------------------------------------------
#  * Python Programming for Data Scientists and Engineers
#  * ICE #5-2 Numpy Array with random values.
#  * Max + Min Value
#  * #11 Chia-Hui Amy Lin
# ------------------------------------------------------------------------------------------------------------
# Library import
import numpy as np

# Assign random values to a 10 x 10 Numpy Array
randArray = np.random.randint(100, size=(10, 10))

# Output the Numpy Array
print("<< 10 x 10 Numpy Array with Random Values >> ")
print(randArray)

# Find the Min and Max Value in this array
print("------------------------------------------------------------------------------")
print("--> MIN Value in the Numpy Array :", np.amin(randArray))
print("--> MAX Value in the Numpy Array :", np.amax(randArray))
print("------------------------------------------------------------------------------")
