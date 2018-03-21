from scipy.sparse.linalg import spsolve
from scipy.sparse import csr_matrix
from oppgave2 import lagA
import numpy as np

intervaller = 10
lengde      = 2                             #meter
bredde      = 0.3                           #meter
tykkelse    = 0.03                          #meter
massetetthet= 480                           #kg/m^3
volum       = lengde * bredde * tykkelse    #m^3
vekt        = volum * massetetthet          #kg

A = csr_matrix(lagA(intervaller))
b = np.array([vekt for x in range(0, intervaller)])
y = spsolve(A, b)

if __name__ == '__main__':
    for i in range(0, len(y)):
        print('y', i+1, ' = ', y[i])
