# Author: Robert Cosentino
# GitHub username: rob-cosentino
# Date: 6/10/23
# Description: This program contains a fully functional Othello game for two players. There is a functional
# board as well as pieces.  The game keeps going until there are no longer any available moves to be made or
# return_winner is called. Players can also request the currently available positions.


class Player:
    """This class is used to create objects representing players of Othello. This class is used by the
    class ‘Othello’ to keep track of each player’s name and color, as well as the winner of the game"""

    def __init__(self, name, color):
        """This method is used to initialize/construct player objects"""
        self._name = name
        self._color = color


class Othello:
    """This class creates an object that represents a game of Othello. It contains information
    About the players as well as the board and the positions of pieces on the board. This
    Class contains the entire game. There is a method to create/add players to the game,
    to print the current board with piece locations, to inform the player of available valid
    moves, and a method to make moves to specified board cells, as well as a method
    To determine if a game has ended and who has won or if there was a tie. The directions
    instance contains a list of tuples that represent each possible direction in which
    a player could move a piece"""
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    def __init__(self):
        """This method is used to initialize/construct an Othello object and play a new
		Game of Othello. An empty list called is initialized called “players” that can be
        filled with player objects to be referenced throughout the game. The 8x8 cell
        Board is also created with the 2 black and 2 white pieces in the correct starting positions"""
        self._players = []
        self._board = [['.' for space in range(10)] for space in range(10)]

        for i in range(10):
            self._board[i][0] = self._board[i][9] = "*"
            self._board[0][i] = self._board[9][i] = "*"

        self._board[4][4] = self._board[5][5] = 'O'
        self._board[4][5] = self._board[5][4] = 'X'

    def print_board(self):
        """This method can be used to print the board in its current state at any point
		Throughout an occurring game. Uses iteration to loop over rows and columns
        to determine if cells on the board contain black/white pieces or are empty"""
        for row in self._board:
            print(' '.join(row))

    def create_player(self, player_name, color):
        """This method utilizes the Player class to initialize a player and add them to the
	    Game"""
        color = 'X' if color == 'black' else 'O'
        player = Player(player_name, color)
        self._players.append(player)

    def return_winner(self):
        """This method determines and returns the winner of the game based on the
		number of each color piece on the board. It implements simple conditional
		Statements that determine whether there were more black, pieces, white
		Pieces, or a tie if the amount of pieces are equal and there are no more possible
		moves"""
        black_count = sum(row.count('X') for row in self._board)
        white_count = sum(row.count('O') for row in self._board)

        black_player = next((player._name for player in self._players if player._color == 'X'), None)
        white_player = next((player._name for player in self._players if player._color == 'O'), None)

        if black_count > white_count:
            return f"The winner is {black_player}"
        elif white_count > black_count:
            return f"The winner is {white_player}"
        else:
            return "The game ended in a tie!"

    def return_available_positions(self, color):
        """This method returns the available positions for the player of the corresponding
		Provided color based on the current state of the board. It uses iteration to loop
        through all of the cells via rows and columns on the current board in order to determine
        what cells are Currently available for the player to place a piece on given the current
        game state and piece positions"""
        available_positions = []
        opponent = 'O' if color[0].upper() == 'X' else 'X'
        for row in range(1, 9):
            for column in range(1, 9):
                if self._board[row][column] == '.':
                    for direction_row, direction_column in self.DIRECTIONS:
                        next_row, next_column = row + direction_row, column + direction_column
                        pieces_to_flip = []
                        while 0 <= next_row < 8 and 0 <= next_column < 8:
                            if self._board[next_row][next_column] == opponent:
                                pieces_to_flip.append((next_row, next_column))
                            elif self._board[next_row][next_column] == color[0].upper():
                                if pieces_to_flip:
                                    available_positions.append((row, column))
                                break
                            else:
                                break
                            next_row, next_column = next_row + direction_row, next_column + direction_column
        return available_positions

    def is_game_over(self):
        """This method determines whether the game is over based
        on the currently available positions. No available positions = game over"""
        black_moves = self.return_available_positions('black')
        white_moves = self.return_available_positions('white')
        return not black_moves and not white_moves

    def make_move(self, color, piece_position):
        """This method is used by play_game and places a piece of specified color
        On a provided position on the board. It also makes use of the
        return_available_positions method in order to determine if the move the player
        Is trying to make is valid or not. If the move is verified as valid, the player’s piece
        Will be placed in the requested cell and the board will be altered. Returns a boolean that
        is provided to the play_game method."""
        current_row, current_column = piece_position
        if self._board[current_row][current_column] != '.':
            return False

        self._board[current_row][current_column] = 'X' if color.lower() == 'black' else 'O'
        opponent = 'O' if color[0].upper() == 'X' else 'X'
        for direction_row, direction_column in self.DIRECTIONS:
            next_row, next_column = current_row + direction_row, current_column + direction_column
            pieces_to_flip = []
            while 0 <= next_row < 8 and 0 <= next_column < 8:
                if self._board[next_row][next_column] == opponent:
                    pieces_to_flip.append((next_row, next_column))
                elif self._board[next_row][next_column] == color[0].upper():
                    for flip_row, flip_column in pieces_to_flip:
                        self._board[flip_row][flip_column] = color[0].upper()
                    break
                else:
                    break
                next_row, next_column = next_row + direction_row, next_column + direction_column
        return True

    def play_game(self, player_color, piece_position):
        """This method is used each time a player wants to make a move and also
		    Determines whether the game has ended after each move. It calls the
		    make_move method in order to receive a boolean value and determine that
		    Determines whether to print an invalid statement or receive the move and
		    Update the board"""
        valid_move = self.make_move(player_color, piece_position)
        if valid_move:
            print("You made a move")
            self.print_board()
            if self.is_game_over():
                self.return_winner()
        else:
            print("Invalid move. Here are your available moves:")
            valid_moves = self.return_available_positions(player_color)
            print(valid_moves)


# game = Othello()
# game.print_board()
# game.create_player("Helen", "white")
# game.create_player("Leo", "black")
# game.play_game("black", (6,5))
# game.print_board()
# game.play_game("white", (6,6))
# game.print_board()