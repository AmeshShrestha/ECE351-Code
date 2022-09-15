################################################################
#                                                              #
# Amesh Shrestha                                               #
# Signals And Systems (ECE 351)                                #
# Lab Section 1                                                #
# Sept 8, 2022                                                 #
#                                                              #
#                                                              #
################################################################

import math
import scipy
import numpy as np
import matplotlib.pyplot as plt

step = 0.1
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

#----------------------Part 1 Task 1----------------------
def f1(t):
    return u(t-2)-u(t-9)

def f2(t):
    return (math.e**(-t))*u(t)

def f3(t):
    return r(t-2)*(u(t-2)-u(t-3))+r(4-t)*(u(t-3)-u(t-4))

a = f1(t)
b = f2(t)
c = f3(t)

plt.figure(figsize = (10, 7))
plt.subplot(2, 1, 1)
plt.plot(t,a,label='f1(t)')
plt.plot(t,b,label='f2(t)')
plt.plot(t,c,label='f3(t)')
plt.grid()
plt.legend(loc='lower right')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.title('Part 1 Plot')


#----------------------Part 2 Task 1----------------------
def conv(f1,f2):
    Nf1 = len(f1)
    Nf2 = len(f2)
    
    f1App = np.append(f1,np.zeros((1,Nf2-1)))
    f2App = np.append(f2,np.zeros((1,Nf1-1)))
    
    result = np.zeros(f1App.shape)
    
    for i in range (Nf1 + Nf2 - 2):
        result[i] = 0
        
        for j in range (Nf1):
            if ((i-j)+1 > 0):
                try:
                    result[i] += f1App[j] * f2App[i-j+1]
                except:
                    print(i-j)
    return result

#----------------------Part 2 Task 2----------------------

Nt = len(t)
tApp = np.append(t,np.zeros((1,Nt-1)))

cf1_f2 = conv(f1(t),f2(t))

plt.figure(figsize = (10, 7))
plt.subplot(3, 1, 1)
plt.plot(tApp, cf1_f2)
plt.grid()
plt.xlabel('t')
plt.ylabel('f(t)')
plt.title('Convalution of f1 and f2')

#----------------------Part 2 Task 3----------------------

cf2_f3 = conv(f2(t),f3(t))

plt.figure(figsize = (10, 7))
plt.subplot(3, 1, 1)
plt.plot(tApp, cf2_f3)
plt.grid()
plt.xlabel('t')
plt.ylabel('f(t)')
plt.title('Convalution of f2 and f3')

#----------------------Part 2 Task 4----------------------

cf1_f3 = conv(f1(t),f3(t))

plt.figure(figsize = (10, 7))
plt.subplot(3, 1, 1)
plt.plot(tApp, cf1_f3)
plt.grid()
plt.xlabel('t')
plt.ylabel('f(t)')
plt.title('Convalution of f1 and f3')
