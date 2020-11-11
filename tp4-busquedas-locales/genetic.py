import random
import numpy as np

#Encuentra no comunes entre los padres
def noncommon(parent1, parent2):
	p = [x1 - x2 for (x1, x2) in zip(parent1, parent2)]

	q = [False if x == 0 else True for x in p]

	c = []
	for x in range(0,len(q)):
	    if q[x]:
	        c.append(x)

	return c


"""
Genera descendencia

pmut = probabilidad de descendencia
noff = numero por pareja
"""
def gen_descendencia(parent1, parent2, noff, pmut, nproblem):
    descendencia = np.zeros((noff,nproblem))
    son = np.zeros(nproblem)

    for j in range(0,noff):
        offseed = np.array([parent1[x] for x in noncommon(parent1, parent2)])
        random.shuffle(offseed)
        

        if random.random() <= 1-pmut:
            for i in range(0,nproblem):
                if i in noncommon(parent1, parent2):
                    son[i] = offseed[0]
                    offseed = np.delete(offseed,0)
                else:
                    son[i] = parent1[i]

        else:
            son = parent1.copy()
            random.shuffle(son)

        descendencia[[j]] = son.copy()

    return descendencia


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


def run_it(board):

	nproblem = len(board)

	# Probabilidad de mutacion
	pmut = 0.3

	# numero de hijos
	noff = nproblem*5

	# Adan y Eva
	par1 = board.copy()
	par2 = par1.copy()
	random.shuffle(par2)


	# A llenar
	fitness = np.zeros(noff)
	max_fitness = []
	descendencia = np.zeros((noff,nproblem))


	b = 0

	while True:
		
		for i in range(0,noff):
			descendencia [[i]] = gen_descendencia(par1, par2, noff, pmut, nproblem)[[i]]
			subject = descendencia [[i]].copy()
			fitness[i] = (hprima(subject))


		fitOrd = fitness.copy()
		np.sort(fitOrd)

		index1 = np.where(fitness == fitOrd[0])[0][0]
		index2 = np.where(fitness == fitOrd[1])[0][1] 

		par1 = descendencia[index1]
		par2 = descendencia[index2]

		b += 1

		if hprima(par1) == 0:

			return par1, b

		if b > 5000 :
			if hprima(par1) < hprima(par2):
				return par1, b
			else:
				return par2, b 

		if hprima(par2) == 0:

			return par2, b


		








