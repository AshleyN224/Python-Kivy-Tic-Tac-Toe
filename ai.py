from random import randint

class Ai:

	def __init__(self, choice):
		self.choice = choice

    # Main function for bot making a move

	def make_move(self, board, winning_combos):
		self.make_random_move(board, winning_combos)  # Do a random move

    # Makes a random move by generating a random integer and checking if the place is free

	def make_random_move(self, board, winning_combos):
		free_buttons = []
		for button in board:  # Simple for loop to extract the free buttons
			if len(button.text.strip()) < 1:  # If the button has no mark, stripping spaces...
				free_buttons.append(button)	
		if board[4] in free_buttons:
			free_buttons[free_buttons.index(board[4])].text = self.choice
			return True			
		for combo in winning_combos:
			if board[combo[0]].text == board[combo[1]].text and board[combo[2]].text == '':
				free_buttons[free_buttons.index(board[combo[2]])].text = self.choice
				return True
			if board[combo[0]].text == board[combo[2]].text and board[combo[1]].text == '':
				free_buttons[free_buttons.index(board[combo[1]])].text = self.choice
				return True
			if board[combo[1]].text == board[combo[2]].text and board[combo[0]].text == '':
				free_buttons[free_buttons.index(board[combo[0]])].text = self.choice
				return True
