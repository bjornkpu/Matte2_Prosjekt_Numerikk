from scipy.sparse.linalg import spsolve
from scipy.sparse import csr_matrix
from oppgave2 import lagA
import numpy as np
from konstanter import * 

def solveAy(n):
	volum = L * w * d
	vekt = volum * p
	A = csr_matrix(lagA(n))
	b = np.array([vekt for x in range(0, n)])
	y = spsolve(A, b)
	return y

if __name__ == '__main__':
    for i in range(0, len(y)):
        print('y', i+1, ' = ', y[i])
