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
	a = [0 for x in range(0,10)]
	index = 0
	for i in [float(j) / 10 for j in range(2, 22, 2)]:
		a[index] += y(i)
		index += 1
	return a
	
def fjerdeDeriverte(n):
	A = lagA(n)
	h = L/n
	yee = ye()
	return (1/h**4) * A * yee

def printYe():
	yePrint = ye()
	for i in range(0, len(yePrint)):
		print(yePrint[i])
		print()

if __name__ == "__main__":	
	printYe()
	print(fjerdeDeriverte(10))