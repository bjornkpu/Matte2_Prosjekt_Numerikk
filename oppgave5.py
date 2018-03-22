from konstanter import *
from oppgave3 import *
import numpy as np

number = 20

for i in range(0, 10):
    y = solveAy(number)
    print(y[0], end='\n\n')
    number *= 2
