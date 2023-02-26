# TicTacToe
Tic-Tac-Toe Game Programming Project

# Introduction
Tic-Tac-Toe is a game in which two players take turns in drawing either an ‘O’ or an ‘X’ in one square of a grid consisting of nine squares. The winner is the first player to get three of the same symbols in a row. This project aims to recreate the game of Tic-Tac-Toe works on a console using Python the code provided implements a Tic Tac Toe game that can be played by a human and a computer. The computer uses a simple implementation of the minimax algorithm to determine the best move to make.

## Technical Details
The project was developed using Python 3.10.10 using visual studio code. This program is a command-line implementation of the classic game Tic-Tac-Toe.

The game starts by asking the user to choose their marker - 'X' or 'O'. Then, the game checks if the user wants to start playing or not. If they do, the game starts with an empty board. The game alternates between the human player and the computer. When it is the human's turn, they choose a position on the board to place their marker. The computer's choice is made using the minimax algorithm. The game ends when either the human or the computer wins or when the board is full. The player is then asked if they want to play again. The minimax algorithm is used to determine the best move for the computer by recursively calculating the best score for all possible moves until the end of the game. The score is determined as follows:

• If the computer wins, the score is 10.<br />
• If the human wins, the score is -10.<br />
• If it is a tie, the score is 0.<br />

The algorithm assumes that the human player always plays optimally.

## Libraries Used 
• Math

## Issues Faced
One of the challenges I encountered while developing the Tic-Tac-Toe game was how to implement an algorithm to check for a win. Initially, I used multiple if statements to check for every possible combination of three marks in a row, column, or diagonal, which wasn't efficient. Afterward, I created an algorithm to compare the marks on the board in each row, column, and diagonal to check for a win, which resulted in a more optimized code that was easier to read and maintain. The algorithm checks each row, column, and diagonal by using a list of tuples, where each tuple contains three positions that represent a row, column, or diagonal. If the marks on these positions are the same, the function returns True. This approach is more elegant and efficient than the previous implementation using multiple if statements.
## Installation and Playing the Game
1.	Install Python 3.10.10
2.	Download the Tic-Tac-Toe project source code
3.	Run the file named tictactoe.py from the command prompt
4.	Choose the drawing ‘X’ or ‘O’ and play the game using the keyboard 

## Functions
• `display_board(board)` - this function takes in a list representing the game board and displays it to the console. The function replaces the numbers on the board with the corresponding marker for each player.. <br />
•	`player_input()` - this function prompts the user to choose their marker ('X' or 'O') and returns both markers as a tuple.<br />
•	`place_marker(board, marker, position)` - this function takes in the game board, the marker, and the position to place the marker on the board. The function modifies the board by placing the marker on the specified position.<br />
•	`space_check(board, position)` - this function takes in the game board and a position and returns True if the position is free and False otherwise.<br />
•	`full_board_check(board)` - this function takes in the game board and returns True if the board is full and False otherwise.<br />
•	`win_check(board, mark)` - this function takes in the game board and a marker and returns True if the marker has won the game and False otherwise.<br />
•	`player_choice(board,player)` - this function takes in the game board and the player type ('human' or 'computer') and returns the position chosen by the player. If the player is human, the function prompts the user to choose a position until a free position is chosen. If the player is computer, the function calls the minimax algorithm to find the best move for the computer player.<br />
•	`replay()` - this function prompts the user to play again and returns True if the user wants to play again and False otherwise.<br />
• `minimax(board, player)` - this function takes in the game board and the current player and returns the best move for the current player as a dictionary containing the position and the score. The function uses recursion to explore all possible moves and their outcomes. The score is calculated based on the outcome of the game (win, lose, or draw). The function returns the move with the highest score for the computer player and the move with the lowest score for the human player.<br />
• `switch_player(player)` - this function takes in the current player and returns the other player.
## Test Cases
Here are some test cases for the Tic-Tac-Toe game:
1.	Win Condition: Verify that the game correctly identifies a win by a player. The test should check whether the game correctly identifies the winning player when three consecutive markers are placed in a row, column or diagonal.
2.	Draw Condition: Verify that the game correctly identifies a draw when the board is full and there is no winner. The test should check whether the game correctly identifies the draw condition.
3.	Player Input: Verify that the player_input() function correctly prompts the user to input their chosen marker, and returns the correct markers for player and computer. The test should check that the function handles invalid inputs and only accepts 'X' or 'O' markers.
4.	Replay Function: Verify that the replay() function works correctly and allows the player to choose whether they want to play again or not. The test should check that the function returns the correct boolean value based on the player's input.
5.	Full Board Check: Verify that the full_board_check() function correctly identifies when the board is full. The test should check whether the function returns True when there are no more empty spaces on the board.


# Conclusion
The Tic-Tac-Toe game programming project was the first game I developed, it was surprisingly fun. During the development process of this code, I gained a deeper understanding of various programming concepts and algorithms. It was a challenging experience, but it allowed me to enhance my skills and knowledge in programming.
Especially the minimax algorithm gave me a new perspective of thinking. I believe it will improve my programming skills for the future.
