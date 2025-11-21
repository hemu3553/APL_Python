# ----------------------------------------------------------------------------
#  * Python Programming for Data Scientists and Engineers
#  * LAB #5-2 Tic Tac Toe Game
#  * #11 Chia-Hui Amy Lin
# ----------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------


class TicTacToeGame(object):
    # Initialize Variables
    blank_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]    # Empty board
    player_one_mark = "X"
    player_two_mark = "O"

    def __init__(self):
        ''' Initialize variables '''
        self.cboard = TicTacToeGame.blank_board
        self.markOne = TicTacToeGame.player_one_mark
        self.markTwo = TicTacToeGame.player_two_mark

    # ------------------------------------------------------------------------------------------------------------
    def draw_board(self):
        ''' Draw the game board when player makes a move each time. '''
        for row in range(len(self.cboard)):
            print('-'*((len(self.cboard[0]))*2 + 1))
            print('|', end='')
            for column in range(len(self.cboard[row])):
                print(self.cboard[row][column], end='|')
            print(' ')
        print('-'*((len(self.cboard[0]))*2 + 1))
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

    # ------------------------------------------------------------------------------------------------------------
    def playerOne(self):
        ''' Mark player 1's move. Player will be prompted again if the input is an invalid format.'''
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
        if self.cboard[player_move_row][player_move_col] == " ":
            self.cboard[player_move_row][player_move_col] = self.player_one_mark
            print("< Player One's Move >")
            TicTacToeGame.draw_board(self)
            TicTacToeGame.referee(self)
            TicTacToeGame.board_full(self)


        # If yes, tell the player the spot is taken. Ask for another prompt
        else:
            print("Oops, spot is taken. Please enter another one!" + "\n")
            flag = True
            TicTacToeGame.playerOne(self)

    # ------------------------------------------------------------------------------------------------------------
    def playerTwo(self):
        ''' Mark player 2's move. Player will be prompted again if the input is an invalid format.'''
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
        if self.cboard[player_move_row][player_move_col] == " ":
            self.cboard[player_move_row][player_move_col] = self.player_two_mark
            print("< Player Two's Move >")
            TicTacToeGame.draw_board(self)
            TicTacToeGame.referee(self)
            TicTacToeGame.board_full(self)

        # If yes, tell the player the spot is taken. Ask for another prompt
        else:
            print("Oops, spot is taken. Please enter another one!" + "\n")
            flag = True
            TicTacToeGame.playerTwo(self)
    # ------------------------------------------------------------------------------------------------------------
    def board_full(self):
        ''' Check if the board is full or not. '''
        full = True
        # Iterate through all rows and columns to see if there's any space left
        # If not, that means the board is all marked
        for check_row in range(len(self.cboard)):
            for check_column in range(len(self.cboard[check_row])):
                if self.cboard[check_row][check_column] == " ":
                    full = False
        if full:
            print("............................ End of Game!!! ...........................")
            exit()
        return full
    # ------------------------------------------------------------------------------------------------------------
    def referee(self):
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
        for check_row in range(len(self.cboard)):
            for check_column in range(len(self.cboard[check_row])):
                if self.cboard[check_row][check_column] == "X":    # Player One
                    player_move[1].append((check_row, check_column))
                elif self.cboard[check_row][check_column] == "O":  # Player Two
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
                            TicTacToeGame.PlayerOne_Won(self)

                    for colVal in count_row_player1.values():
                        # 3 Same Column Number - Strike Vertical
                        if colVal == 3:
                            TicTacToeGame.PlayerOne_Won(self)
                # For Player Two
                elif key == 2:
                    # Check Diagonal Strike
                    if (1, 1) in val:
                        if (0, 0) in val and (2, 2) in val:
                            TicTacToeGame.PlayerTwo_Won(self)

                        elif (0, 2) in val and (2, 0) in val:
                            TicTacToeGame.PlayerTwo_Won(self)

                    # Check Vertical and Horizontal Strike
                    count_row_player2[oneRow] = count_row_player2.get(oneRow, 0) + 1  # Count occurences of Row Numbers
                    count_col_player2[oneCol] = count_col_player2.get(oneCol, 0) + 1  # Count occurences of Column Numbers
                    for rowVal in count_row_player2.values():
                        # 3 Same Row Number - Strike Horizontal
                        if rowVal == 3:
                            TicTacToeGame.PlayerTwo_Won(self)

                    for colVal in count_row_player2.values():
                        # 3 Same Column Number - Strike Vertical
                        if colVal == 3:
                            TicTacToeGame.PlayerTwo_Won(self)
    # ------------------------------------------------------------------------------------------------------------
    def header(self):
        ''' Print out Header for the game. '''
        print("[  Welcome to Tic Tac Toe Game! Ready to have some battles? ;) ]")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    # ------------------------------------------------------------------------------------------------------------
    def PlayerOne_Won(self):
        ''' Announcement when Player One won the game. '''
        print("\n")
        print("****************** WE GOT A WINNER! Player One won! ******************", "\n")
        print("............................ End of Game!!! ...........................")
        exit()
    # ------------------------------------------------------------------------------------------------------------
    def PlayerTwo_Won(self):
        ''' Announcement when Player Two won the game. '''
        print("\n")
        print("****************** WE GOT A WINNER! Player Two won! ******************", "\n")
        print("............................ End of Game!!! ...........................")
        exit()

    # ------------------------------------------------------------------------------------------------------------
    def main(self):
        ''' Main Function to Start the Game. '''
        # Start of the Game : Header
        TicTacToeGame.header(self)
        while TicTacToeGame.board_full(self) is not True:
            # Player #1 goes first
            TicTacToeGame.playerOne(self)

            # Then Player #2
            TicTacToeGame.playerTwo(self)

# __________________________________________ MAIN __________________________________________________
# Start the game!
if __name__ == '__main__':
    gameOn = TicTacToeGame()
    gameOn.main()

