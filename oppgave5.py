from konstanter import *
from oppgave3 import *
from oppgave4_d import lagVektor
import numpy as np


def finnFeil(n):
    volum = L * w * d
    vekt = volum * p
    b = np.array([vekt for x in range(n)])
    y = solveAy(n, b)

    return y[Lint]


for i in range(1, 12):
    n = 10 * 2 ** i
    print(n)
    a = lagVektor(n)
    feil = finnFeil(n)
    print(feil)
    print(feil - a[Lint])
    print()
