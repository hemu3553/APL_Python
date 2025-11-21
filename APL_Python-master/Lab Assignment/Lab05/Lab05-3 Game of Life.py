# ----------------------------------------------------------------------------
#  * Python Programming for Data Scientists and Engineers
#  * LAB #5-3 Game Of Life
#  * #11 Chia-Hui Amy Lin
# ----------------------------------------------------------------------------
# Show calculation for birth, survive, death

# Library import
import numpy as np

# Living cell surrounded by more than 3 living cells -- die
def overpopulation():

# Living cell surrounded by 2 or 3 living cells -- survives
def stasis():

# Living cell surrounded by < 2 living cells -- die
def underpopulation():

# Dead cell surrounded by cells = 3 -- live
def reproduction():

# Assign random values to a 10 x 10 Numpy Array
randArray = np.random.randint(100, size=(10, 10))

# Output the Numpy Array
print("<< 10 x 10 Numpy Array with Random Values >> ")
print(randArray)
