from oppgave4 import *
from konstanter import *
import numpy as np
from scipy.sparse import lil_matrix


def lagVektor(n):
    b = np.ones(n)
    b = [f/(E*I) for i in range(n)]
    return b


def finnForoverfeil(x, xa):
    out = []
    for i in range(0, len(x)):
        out.append(abs(x[i]-xa[i]))
    return out


def finnRelativForoverfeil(x, xa):
    out = []
    for i in range(0, len(x)):
        out.append((abs(x[i] - xa[i]))/(abs(x[i])))
    return out


def finnFeilforstoring(RFE, RBE):
    out = []
    for i in range(0, len(RFE)):
        out.append(RFE[i]/RBE)
    return out


def finnKondisjonstallet(A):
    return abs(A)*abs(np.linalg.inv(A))


if __name__ == "__main__":
    n = 10
    RBE = 2**(-52)

    vektor = lagVektor(n)
    fjerde = fjerdeDeriverte(n)

    FE = finnForoverfeil(vektor, fjerde)
    RFE = finnRelativForoverfeil(vektor, fjerde)
    EMF = finnFeilforstoring(RFE, RBE)      #Error Magnification Factor

    print(FE)
    print(RFE)
    print(EMF)

    A = lagA(n)
    Akond = finnKondisjonstallet(A)

    print(Akond)






