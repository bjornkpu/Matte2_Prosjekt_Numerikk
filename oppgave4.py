import scipy as sp
import numpy as np
from oppgave2 import lagA
from konstanter import *

def y(x):
	konstantledd = f/(24*E*I)
	forsteledd = x**2
	andreledd = x**2 - 4*L*x + 6*(L**2)
	return konstantledd * forsteledd * andreledd
	
def ye():
	ye = [0 for x in range(0,10)]
	iterate = 0.2

	for i in range(10):
		ye[i] = y(iterate)
		iterate += 0.2
		
	return ye
	
def fjerdeDeriverte(h):
	A = lagA(10)
	yee = ye()
	return 1/h**4 * A * yee

def printYe():
	yePrint = ye()

	for i in range(0, len(yePrint)):
		print(yePrint[i])
		print()

print(fjerdeDeriverte(10**3))