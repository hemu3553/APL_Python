# ------------------------------------------------------------------------------------------------------------
#  * Python Programming for Data Scientists and Engineers
#  * LAB #3-3 Tic Tac Toe Game
#  * #11 Chia-Hui Amy Lin
# ------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------
def draw_board(board_array):
    ''' Draw the game board when player makes a move each time. '''
    for row in range(len(board_array)):
        print('-'*((len(board_array[0]))*2 + 1))
        print('|', end='')
        for column in range(len(board_array[row])):
            print(board_array[row][column], end='|')
        print(' ')
    print('-'*((len(board_array[0]))*2 + 1))
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

# ------------------------------------------------------------------------------------------------------------
def player(player_move_board, mark):
    ''' Mark player's move. Player will be prompted again if the input is an invalid format.'''
    flag = False
    while True:
        try:
            # Prompt user for row and column number that he/she wants to mark the move : Format (row, column)
            player_move_row, player_move_col = map(int, input("Please make your move with numbers of (row, column) :").split(","))

        # Handling Error Input
        except ValueError or TypeError or IndexError:
            print("Invalid input. Please enter an INTEGER." + "\n")
            flag = True
        else:
            break
    # Check if the spot that the player chose is occupied or not
    # If not, mark the player's move
    if player_move_board[player_move_row][player_move_col] == " ":
        player_move_board[player_move_row][player_move_col] = mark

    # If yes, tell the player the spot is taken. Ask for another prompt
    else:
        print("Oops, spot is taken. Please enter another one!" + "\n")
        flag = True
        player(player_move_board, mark)

    return player_move_board

# ------------------------------------------------------------------------------------------------------------
def board_full(current_board):
    ''' Check if the board is full or not. '''
    full = True
    # Iterate through all rows and columns to see if there's any space left
    # If not, that means the board is all marked
    for check_row in range(len(current_board)):
        for check_column in range(len(current_board[check_row])):
            if current_board[check_row][check_column] == " ":
                full = False
    return full

# ------------------------------------------------------------------------------------------------------------
def referee(current_board):
    ''' Referee to call a player the winner of the game. '''
    # Keep track of both players' move ( coordinates )
    player_move = {1: [], 2: []}
    # Dictionaries as trackers for occurences of rows and columns for both players
    # Player One Tracker
    count_row_player1 = {}
    count_col_player1 = {}
    # Player Two Tracker
    count_row_player2 = {}
    count_col_player2 = {}

    # Find the coordinates that the player marked their move
    for check_row in range(len(current_board)):
        for check_column in range(len(current_board[check_row])):
            if current_board[check_row][check_column] == "X":    # Player One
                player_move[1].append((check_row, check_column))
            elif current_board[check_row][check_column] == "O":  # Player Two
                player_move[2].append((check_row, check_column))

    # Call out the winner when the conditions are met
    for key, val in player_move.items():
        for oneRow, oneCol in val:
            # For Player One
            if key == 1:
                # Check Diagonal Strike
                if (1, 1) in val:
                    if (0, 0) in val and (2, 2) in val:
                        winner = "Player One"
                        return winner
                    elif (0, 2) in val and (2, 0) in val:
                        winner = "Player One"
                        return winner
                # Check Vertical and Horizontal Strike
                count_row_player1[oneRow] = count_row_player1.get(oneRow, 0) + 1  # Count occurences of Row Numbers
                count_col_player1[oneCol] = count_col_player1.get(oneCol, 0) + 1  # Count occurences of Column Numbers
                for rowVal in count_row_player1.values():
                    # 3 Same Row Number - Strike Horizontal
                    if rowVal == 3:
                        winner = "Player One"
                        return winner
                for colVal in count_row_player1.values():
                    # 3 Same Column Number - Strike Vertical
                    if colVal == 3:
                        winner = "Player One"
                        return winner
            # For Player Two
            elif key == 2:
                # Check Diagonal Strike
                if (1, 1) in val:

                    if (0, 0) in val and (2, 2) in val:
                        winner = "Player Two"
                        return winner
                    elif (0, 2) in val and (2, 0) in val:
                        winner = "Player Two"
                        return winner
                # Check Vertical and Horizontal Strike
                count_row_player2[oneRow] = count_row_player2.get(oneRow, 0) + 1  # Count occurences of Row Numbers
                count_col_player2[oneCol] = count_col_player2.get(oneCol, 0) + 1  # Count occurences of Column Numbers
                for rowVal in count_row_player2.values():
                    # 3 Same Row Number - Strike Horizontal
                    if rowVal == 3:
                        winner = "Player Two"
                        return winner
                for colVal in count_row_player2.values():
                    # 3 Same Column Number - Strike Vertical
                    if colVal == 3:
                        winner = "Player Two"
                        return winner

# ------------------------------------------------------------------------------------------------------------
def main():
    ''' Main Function to Start the Game. '''
    # Initialize Variables
    blank_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]    # Empty board
    player_one_mark = "X"
    player_two_mark = "O"

    # Start of the Game : Header
    print("[  Welcome to Tic Tac Toe Game! Ready to have some battles? ;) ]")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

    # Player #1 goes first
    player_one_prompt = False
    while True:
        print("< Player One's Move >")
        update_board = player(blank_board, player_one_mark)
        # Continue when the input is valid
        if update_board:
            # Output current board with player's move
            draw_board(update_board)

            # Check if the board is full at this point or not
            check_full = board_full(update_board)

            # Call function referee to see if the player wins on his/her move or not.
            # If yes, game over!
            winOrNot = referee(update_board)

            # Announce the Winner
            if winOrNot == "Player One":
                print("\n")
                print("****************** WE GOT A WINNER! Player One won! ******************", "\n")
                print("............................ End of Game!!! ...........................")
                exit()

            if check_full:
                print("...................... Seems like a TIE! End of Game!!! .....................")
                break
        else:
            player_one_prompt = True

    # Player #2's Turn
        player_two_prompt = False
        while True:
            print("< Player Two's Move >")
            update_board = player(update_board, player_two_mark)
            # Continue when the input is valid
            if update_board:
                # Output current board with player's move
                draw_board(update_board)

                # Check if the board is full at this point or not
                check_full = board_full(update_board)
                # Call function referee to see if the player wins on his/her move or not.
                # If yes, game over!
                winOrNotTwo = referee(update_board)

                # Announce the Winner
                if winOrNotTwo == "Player Two":
                    print("\n")
                    print("****************** WE GOT A WINNER! Player Two won! ******************", "\n")
                    print("............................ End of Game!!! ...........................")
                    exit()

                if check_full:
                    print("............................ End of Game!!! ...........................")
                    break
                break
            else:
                player_two_prompt = True

# __________________________________________ MAIN __________________________________________________
# Start the game! Call main function
main()
