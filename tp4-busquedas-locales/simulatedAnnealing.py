import numpy as np
import random as rd
import math

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


#a randomly selected successor of current 

def choseNewN(board):

    while True:
        x = rd.randint(0, len(board) - 1)
        y = rd.randint(0, len(board) - 1)

        if board[x] == y:
            continue

        board_prima = board.copy()
        board_prima[x] = y

        return board_prima


def h(board):
    solution = board.copy()
    current_min = hprima(solution)
    
    cont = 0
    t= 3000
    while t > 0.00000000000000000001:
    	cont += 1
    	t *= 0.99

    	board_prima = choseNewN(solution)

    	n = hprima(board_prima)

    	if n >= current_min:

        	d = hprima(board_prima) - current_min
        	p = math.exp(-d/t)

        	if (rd.choices([0, 1], [1-p,p], k=1) == [1]):
        		solution = board_prima.copy()

    	elif n < current_min:
        	solution = board_prima.copy()
        	if n == 0:
        		return solution, cont

    return solution, cont
        	       
def run_it(board):

    solution, control = h(board)

    #print("Simulated Annealing n states: ", control)

    return solution, control 


