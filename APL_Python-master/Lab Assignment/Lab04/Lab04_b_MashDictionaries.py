# ------------------------------------------------------------
#  * Python Programming for Data Scientists and Engineers
#  * LAB #4-b Mash Dictionaries
#  * #11 Chia-Hui Amy Lin
# ------------------------------------------------------------

# Dictionary
from statistics import mean


# Function
def mash(input_dict):
    ''' Function for mashing keys with integer values into one and update the current dictionary in the list. '''
    for idx in range(len(input_dict)):
        intList = []
        popList = []
        mash = {}
        keyMash = ""
        for key, val in inputList[idx].items():
            if type(val) is int:
                intList.append(val)
                popList.append(key)
                keyMash += (key + ",")
        mash[keyMash] = mean(intList)
        input_dict[idx].update(mash)
        for num in range(len(popList)):
            input_dict[idx].pop(popList[num])
    return input_dict

# Input value
inputList = [{"course": "coffee", "Crows": 3, "Starbucks": 7},
             {"course": "coffee", "Crows": 4, "Starbucks": 8},
             {"course": "coffee", "Crows": 3, "Starbucks": 5}]
print("< #4-b Mash Dictionaries >")

# Call function to mash/update the original list
inputList = mash(inputList)

# Output the result
print("Updated Input :", inputList)
