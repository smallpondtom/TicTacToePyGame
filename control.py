from math import inf
from random import choice

CROSS = -1
CIRCLE = 1	
NCIRCLE = 0
INCREMENT = 10
INITBOARD = [
		    [0, 0, 0],
		    [0, 0, 0],
		    [0, 0, 0],
			]

class mai:
	def __init__(self, game, depth, play):
		self.__depth = depth
		self.__game = game
		self.__play = play

	def minimax(self, state, depth, play):
		if play == self.__play:
			best = [-1, -1, -inf]
		else:
			best = [-1, -1, +inf]

		if depth == 0 or tictactoe.game_over(state):
			score = self.evaluate(state)
			return [-1, -1, score]

		for cell in tictactoe.empty_cells(state):
			x, y = cell[0], cell[1]
			state[x][y] = play
			score = self.minimax(state, depth - 1, tictactoe.oppTurn(play))
			state[x][y] = 0
			score[0], score[1] = x, y

			if play == self.__play:
				if score[2] > best[2]:
					best = score
			else:
				if score[2] < best[2]:
					best = score
		return best

	def evaluate(self, state):
		if tictactoe.wins(state, self.__play):
			score = INCREMENT
		elif tictactoe.wins(state, tictactoe.oppTurn(self.__play)):
		 	score = -INCREMENT
		else:
			score = 0
		return score

	def move(self):
		board = self.__game.getBoard()
		if self.__game.done():
			return
		else:
			move = self.minimax(board, self.__depth, self.__play)
			x, y = move[0], move[1]
		return x, y, self.__play

	def changeDepth(self, depth):
		self.__depth = depth

class tictactoe:
	def __init__(self, board=INITBOARD):
		self.__board = list(map(list, INITBOARD))

	def __str__(self):
		return str(self.__board)

	def clear(self):
		self.__board = list(map(list, INITBOARD))

	def valid(self, x, y):
		if [x, y] in tictactoe.empty_cells(self.__board):
			return True
		else:
			return False

	def update(self, x, y, play):
		if self.valid(x, y):
			self.__board[x][y] = play
			return True
		else:
			return False

	def game_over(state):
		return tictactoe.wins(state, CROSS) or tictactoe.wins(state, CIRCLE) or len(tictactoe.empty_cells(state)) == 0

	def done(self):
		return tictactoe.game_over(self.__board)

	def wins(state, play):
		win_state = [
	        [state[0][0], state[0][1], state[0][2]],
	        [state[1][0], state[1][1], state[1][2]],
	        [state[2][0], state[2][1], state[2][2]],
	        [state[0][0], state[1][0], state[2][0]],
	        [state[0][1], state[1][1], state[2][1]],
	        [state[0][2], state[1][2], state[2][2]],
	        [state[0][0], state[1][1], state[2][2]],
	        [state[2][0], state[1][1], state[0][2]],
	    ]
		if [play, play, play] in win_state:
			return True
		else:
			return False

	def game(self, play):
		return tictactoe.wins(self.__board, play)

	def empty_cells(state):
		cells = []
		for x, row in enumerate(state):
			for y, cell in enumerate(row):
				if cell == NCIRCLE:
					cells.append([x, y])
		return cells

	def draw(self):
		return len(tictactoe.empty_cells(self.__board)) == 0 and not tictactoe.wins(self.__board, CROSS) and not tictactoe.wins(self.__board, CIRCLE)

	def empty(self):
		return tictactoe.empty_cells(self.__board)

	def getBoard(self):
		return list(map(list, self.__board))

	def oppTurn(play):
		if play == CIRCLE:
			return CROSS
		else:
			return CIRCLE

	def getCross():
		return CROSS

	def getCircle():
		return CIRCLE