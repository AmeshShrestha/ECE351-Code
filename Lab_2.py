################################################################
#                                                              #
# Amesh Shrestha                                               #
# Signals And Systems (ECE 351)                                #
# Lab Section 1                                                #
# Sept 8, 2022                                                 #
#                                                              #
#                                                              #
################################################################

import numpy as np
import matplotlib.pyplot as plt

step = 1e-2
t = np.arange(0, 10+step, step)

def func1(t):
    y = np.zeros(t.shape)
    
    for i in range(len(t)):
        y[i] = np.cos(t[i])
    return y

y = func1(t)

plt.figure(figsize = (10, 7))
plt.subplot(2, 1, 1)
plt.plot(t, y)
plt.grid()
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Cosine Function')


# part 2
# y= r(t)-r(t-3)+5u(t-3)-2u(t-6)-2r(t-6)

t = np.arange(-5, 10+step, step)

def u(t):
    y = np.zeros(t.shape)
    
    for i in range(len(t)):
        if t[i] < 0:
            y[i] = 0
        else:
            y[i] = 1
    return y

def r(t):
    y = np.zeros(t.shape)
    
    for i in range(len(t)):
        if t[i] < 0:
            y[i] = 0
        else:
            y[i] = t[i]
    return y

def func2(t):
    return r(t)-r(t-3)+5*u(t-3)-2*u(t-6)-2*r(t-6)

y = func2(t)

plt.figure(figsize = (10, 7))
plt.subplot(2, 1, 1)
plt.plot(t[range(len(y))], y)
plt.grid()
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Plot for Lab 2'

