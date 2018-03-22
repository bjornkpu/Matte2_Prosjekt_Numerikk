from oppgave2 import *
from oppgave3 import *
from konstanter import *

def f(n, vekt, lengde):
	A = lagA(n)
	a = [0 for x in range(0, n)]
	for i in range(len(a)):
		if i > L-lengde:
			a[i] = -g * (vekt/lengde)
	
	return a
	

	
if __name__ == "__main__":
	n = 20
	b = f(n, 50, 0.3)
	y = solveAy(n, b)
	for i in range(len(y)):
		print('y',i+1,' = ',y[i])