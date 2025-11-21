'''
  * Python Programming for Data Scientists and Engineers
  * ICE #3-1 Draw a Customized Game Board.
  * Prompt user for the size of the game board.
  * Output the shape.
  * #11 Chia-Hui Amy Lin
'''


# -------------------------------------------------- Functions --------------------------------------------------
# Function for printing horizontal line
def print_horiz_line(horizon_num):
    return print(horizon_num * " ---")


# Function for printing vertical line
def print_vert_line(vertical_num):
    return print((vertical_num + 1) * "|   ")


# Function for checking whether input is an integer or not. Return size
def check_input():
    flag = False
    while True:
        size_prompt = input("Please enter the size for your game board : ")
        try:
            size_prompt = int(size_prompt[0])
        except ValueError or TypeError:
            print("Invalid input. Please enter an INTEGER." + "\n")
            flag = True
        else:
            break
    return size_prompt

# -------------------------------------------------- Main --------------------------------------------------
# Variable
count = 0

# Call function check_input for game board size
size = check_input()

# Output Graph
print("=======================================================")
print("<<Game Board Size", size, "x", size, ">>")
while count < size:
    print_horiz_line(size)
    print_vert_line(size)
    count += 1
print_horiz_line(size)
print("=======================================================")
