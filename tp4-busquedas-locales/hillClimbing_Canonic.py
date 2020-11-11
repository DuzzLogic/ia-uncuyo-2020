import numpy as np
import random as rd

"""
x: column
y: row
"""

# h(t)
def hprima(board):
	n = 0

	for x in range(0,len(board)):
		c = x + 1
		for y in range(c,len(board)):

			#same row or same diagonal
			if board[x] == board[y] or abs(y - x) == abs(board[y] - board[x]):
				n += 1

	return n


def h(board):
	current_min = hprima(board)
	toSee = [board]


	for x in range(0,len(board)):
		for y in range(0,len(board)):

			if board[x] == y:
				continue

			board_prima = board.copy()
			board_prima[x] = y 

			n = hprima(board_prima)
			
			if n < current_min:
				current_min = n
				toSee = [board_prima]
			elif n == current_min:
				toSee.append(board_prima)
	
	board = toSee[rd.randint(0,len(toSee)-1)].copy()

	return board, len(toSee)



def run_it(board):
	control = 0
	while True:
		old_board = board.copy()

		board , optimal= h(board)		

		control +=1


		if optimal == 1:
			#print("Hill Climbing n states: ", control)
			break

		if control > 1000:
			break

	return board, control


