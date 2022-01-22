import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.cos(x/3)

def d(Y, x):
    return (Y[x-3]+8*Y[x-2]-115*Y[x-1]+115*Y[x+1]-8*Y[x+2]-Y[x+3])/192

def mid(Y0):
    n0 = len(Y0)
    Y1 = [d(Y0, x) for x in range(3, n0-3)]
    n1 = len(Y1)
    Y2 = [d(Y1, x) for x in range(3, n1-3)]
    n2 = len(Y2)
    Ydemi = np.zeros(2*n0)
    for i in range(6, 2*(n0-12), 2):
        Ydemi[i] = Y0[i//2]
    for i in range(6, 2*(n0-13), 2):
        Ydemi[i+1] = (8*(Y0[i//2]+Y0[1 + (i//2)])+4*(Y1[i//2]-Y1[1 + (i//2)])+2*(Y2[i//2]+Y2[1 + (i//2)]))/16
    return Ydemi

X = np.arange(60)
Y = f(X)
Xdemi = np.arange(120)
Ydemi = mid(Y)
Xquart = np.arange(240)
Yquart = mid(Ydemi)

plt.stem(Xquart, Yquart, markerfmt ='bx', linefmt='b')
plt.stem(X*4, Y, markerfmt ='rx', linefmt='r')
plt.show()
