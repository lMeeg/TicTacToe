# TicTacToe
Tic-Tac-Toe Game Programming Project

# Introduction
Tic-Tac-Toe is a game in which two players take turns in drawing either an ‘O’ or an ‘X’ in one square of a grid consisting of nine squares. The winner is the first player to get three of the same symbols in a row. This project aims to recreate the game of Tic-Tac-Toe works on a console using Python

## Technical Details
The project was developed using Python 3.10.10 using visual studio code. This program is a command-line implementation of the classic game Tic-Tac-Toe.
##Libraries Used 
The program doesn't rely on any external libraries.
## Issues Faced
One of the challenges faced while developing the Tic-Tac-Toe game was implementing the algorithm to check for a win. The code required a function that would check each possible combination of three marks in a row, column, or diagonal, and return true if they all had the same mark. Initially, I had to implement multiple if statements to check each combination, but this approach was not efficient. Therefore, I had to come up with a better algorithm to check for a win. Eventually, I implemented an elegant and more efficient algorithm that checked for a win by comparing the marks on the board in each row, column, and diagonal. This approach resulted in a more optimized code that was easier to read and maintain.
##Installation and Playing the Game
1.	Install Python 3.10.10
2.	Download the Tic-Tac-Toe project source code
3.	Run the file named tictactoe.py from the command prompt
4.	Choose the drawing ‘X’ or ‘O’ and play the game using the keyboard 

## Functions
• `display_board(board)` - this function takes in the current board as an input, and prints it to the console. The board is a list with 10 elements, where the first element is ignored, and the remaining 9 elements are either empty spaces '#', 'X', or 'O'. <br />
•	`player_input()` - this function prompts the user to choose their marker, 'X' or 'O'. It returns a tuple with the two player's markers.<br />
•	`place_marker(board, marker, position)` - this function takes in the current board, the player's marker ('X' or 'O'), and the position where the marker should be placed. It updates the board and returns it.<br />
•	`space_check(board, position)` - this function takes in the current board and the position being checked, and returns True if the position is empty, and False otherwise.<br />
•	`full_board_check(board)` - this function takes in the current board, and returns True if the board is full, and False otherwise.<br />
•	`win_check(board, mark)` - this function takes in the current board and a player's marker ('X' or 'O'), and returns True if the player has won, and False otherwise.<br />
•	`player_choice(board)` - this function prompts the player to choose an empty position on the board, and returns the position as an integer.<br />
•	`replay()` - this function prompts the user if they want to play again, and returns True if they do, and False otherwise.<br />
## Test Cases
Here are some test cases for the Tic-Tac-Toe game:
1.	Win Condition: Verify that the game correctly identifies a win by a player. The test should check whether the game correctly identifies the winning player when three consecutive markers are placed in a row, column or diagonal.
2.	Draw Condition: Verify that the game correctly identifies a draw when the board is full and there is no winner. The test should check whether the game correctly identifies the draw condition.
3.	Player Input: Verify that the player_input() function correctly prompts the user to input their chosen marker, and returns the correct markers for both players. The test should check that the function handles invalid inputs and only accepts 'X' or 'O' markers.
4.	Replay Function: Verify that the replay() function works correctly and allows the player to choose whether they want to play again or not. The test should check that the function returns the correct boolean value based on the player's input.
5.	Full Board Check: Verify that the full_board_check() function correctly identifies when the board is full. The test should check whether the function returns True when there are no more empty spaces on the board.


# Conclusion
The Tic-Tac-Toe game programming project was the first game I developed, it was surprisingly fun. During the development process of this code, I gained a deeper understanding of various programming concepts and algorithms. It was a challenging experience, but it allowed me to enhance my skills and knowledge in programming.
