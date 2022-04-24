import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random
from random import randint as rand
import sys
i = 0 + 1j

def FFT(P):
    n = len(P)
    if n == 1:
        return P
    w = math.e**((2*math.pi*i)/n)
    Pe = []
    Po = []
    for index,valor in enumerate((P)):
        if index % 2 == 0:
            Pe.append(valor)
        else:
            Po.append(valor)
    #print(Pe,Po)
    Ye = FFT(Pe)
    Yo = FFT(Po)
    Y = [0] * n
    for j in range(int(n/2)):
        Y[j] = Ye[j] + (w**j)*Yo[j]
        Y[j + int(n/2)] = Ye[j] - (w**j)*Yo[j]
    return Y
    
if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) < 2:
        P = []
        for t in range(1024):
            P.append(math.sin(2*math.pi*500*t/1024))
        #plt.plot(range(1024),P)
        #plt.show()
        #print(FFT(P))
        for t in range(1024):
            P[t] += math.sin(2*math.pi*250*t/1024)
        sal = FFT(P)
        final = []
        for i in range(int(len(sal)/2)):
            final.append(abs(sal[i]))
        plt.plot(range(512),final)
        plt.show()
    else:
        print("Demasiados argumentos")
        print(sys.argv)
            
