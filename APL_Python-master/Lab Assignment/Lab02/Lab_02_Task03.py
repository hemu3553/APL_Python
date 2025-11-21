'''
  * Python Programming for Data Scientists and Engineers
  * LAB #2-3 Find numbers between 1500 - 2700 that are divisible by 7 and are multiples of 5
  * #11 Chia-Hui Amy Lin
'''

# Variables : Empty list for numbers that match, number starts with 1500
numberList = []
num_start = 1500

# Check numbers between 1500 - 2700 & put those that are divisible by 7 and are multiples of 5 to the list
while num_start <= 2700:
    if num_start % 7 == 0 and num_start % 5 == 0:
        numberList.append(num_start)
    num_start += 1

# Output 10 numbers per line
print("Numbers between 1500 & 2700 divisible by 7 and are multiples of 5 :")
for idx in range(0, len(numberList), 10):
    print(numberList[idx:idx + 10])
