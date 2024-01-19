# CS162: Introduction to Python Pt.2 Final Project. Oregon State University

# Othello (Reversi) Implementation in Python
This repository contains a Python implementation of the classic board game Othello, also known as Reversi. The game is played on an 8x8 grid, and the goal is to have more pieces of your color on the board than your opponent by the end of the game.

## Classes
The implementation consists of two main classes:

### 1. Player
This class represents a player in the game of Othello. It keeps track of the player's name and color.
Attributes:
* 'name': The name of the player
* 'color': The color of the player's pieces (black or white)

### 2. Othello 
This class represents the game itself, containing all the logic for playing the game, tracking the board state, and determining the winner.

Methods
* __init__: Initializes a new game with an empty board and starting pieces.
* print_board: Prints the current state of the board.
* create_player: Adds a new player to the game.
* return_winner: Determines and returns the winner of the game based on the number of each color piece on the board.
* return_available_positions: Returns the available positions for a player based on the current state of the board.
* is_game_over: Determines if the game has ended based on the availability of valid moves.
* make_move: Attempts to place a piece on the board and flips the opponent's pieces accordingly.
* play_game: Facilitates a player making a move and updates the game state.


## Made By
* Rob Cosentino

### Contact:
* robert.cosentino1@gmail.com
* linkedin.com/in/rob-cosentino/