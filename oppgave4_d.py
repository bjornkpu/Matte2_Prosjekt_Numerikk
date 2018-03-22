from oppgave4 import *
from konstanter import *


def lagVektor(n):
    konstantledd = f / (E * I)
    a = [konstantledd for x in range(0, n)]
    return a


if __name__ == "__main__":
    ye = ye()
    v = lagVektor(10)
    for i in range(0, 10):
        forskjell = ye[i] - f / (E * I)
        print('i', i, '=', forskjell)
