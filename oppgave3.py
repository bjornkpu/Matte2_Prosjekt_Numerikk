from scipy.sparse.linalg import spsolve
from scipy.sparse import csr_matrix
from oppgave2 import lagA
import numpy as np
from konstanter import *


<<<<<<< HEAD
def solveAy(n, b):
	A = csr_matrix(lagA(n))
	h = L/n
	fac = h**4/(E*I)
	for i in range(len(b)):
		b[i] *= fac
	y = spsolve(A, b)
	return y

if __name__ == '__main__':
	volum = L * w * d
	vekt = volum * p
	n = 10
	b = np.array([vekt for x in range(n)])
	y = solveAy(n, b)
	for i in range(len(y)):
		print('y',i+1,' = ',y[i])
=======
def solveAy(n):
    volum = L * w * d
    vekt = volum * p
    A = csr_matrix(lagA(n))
    b = np.array([vekt for x in range(0, n)])
    h = L / n
    factor = h ** 4 / (E * I)
    b *= factor
    y = spsolve(A, b)
    return y


if __name__ == '__main__':
    y = solveAy(10)
    for i in range(0, len(y)):
        print('y', i + 1, ' = ', y[i])
>>>>>>> 9fb52f5a3f66edabf3de0c0ac745b77339632f8e
