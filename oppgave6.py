import matplotlib.pyplot as plt
import math as m
from konstanter import *
from oppgave4 import lagY
import numpy as np

def sinusY(x):
	y = lagY(x)
	konstantleddet = (g*100*L)/(E*I*m.pi)
	sinusleddet = (L**3/m.pi**3)*np.sin((m.pi/L)*x)
	sisteleddet = -(x**3)/6 + (L*x**2)/2 - (L**2*x)/m.pi**2
	return y + (konstantleddet*(sinusleddet + sisteleddet))


x = 10*2**1
y = sinusY(x)

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)
	
if __name__ == "__main__":
	X1 = np.linspace(10*2**1, 10*2**11)
	Y1 = sinusY(X1)
	Y2 = (L/X1)
	
	plt.plot(Y1) #sinus-funksjon
	plt.plot(Y2) #teoretisk feil
	plt.show()