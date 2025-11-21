# ----------------------------------------------------------------------------
#  * Python Programming for Data Scientists and Engineers
#  * LAB #4-a Ordered Dictionary ( Use OrderedDict from collections library )
#  * #11 Chia-Hui Amy Lin
# ----------------------------------------------------------------------------

# Library
from collections import OrderedDict

# A predefined unordered dictionary
alphabet_unorder = {"A": "Fuji Apple", "C": "Black Coffee", "B": "Chocolate Banana", "E": "Scramble Egg", "S": "Vanilla Sorbet"}

# Sort the dictionary by Key
alphabet_ordered_key = OrderedDict(sorted(alphabet_unorder.items(), key=lambda x: x[0]))
# Sort the dictionary by Value
alphabet_ordered_val = OrderedDict(sorted(alphabet_unorder.items(), key=lambda y: y[1]))

# Output the sorted results in type dictionary
print("< Ordered by Key >", "\n", dict(alphabet_ordered_key))
print("\n")
print("< Ordered by Val >", "\n", dict(alphabet_ordered_val))
