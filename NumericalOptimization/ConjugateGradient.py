#!/usr/bin/env python
# coding: utf-8

# In[1]:


from mpl_toolkits import mplot3d

import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt
from sympy import *
from scipy import *


# ### Define the Matrix X, Y

# In[2]:


def derivateA(X, Y, A, B):
    newA = np.zeros((3, 3))
    newA = np.matrix(newA)
    for i in range(0, 3):
        _X = np.transpose(X[i])
        _Y = np.transpose(Y[i])
        _B = np.transpose(B)

        newA += (2 * (_B + A * _X - _Y) * X[i])
    return newA


# In[3]:


def derivateB(X, Y, A, B):
    newB = np.zeros((3, 1))
    newB = np.matrix(newB)
    for i in range(0, 3):
        _X = np.transpose(X[i])
        _Y = np.transpose(Y[i])
        _B = np.transpose(B)
        newB += (2 * (_B + A * _X - _Y))
    return newB


# In[4]:


def LValue(X, Y, A, B):
    norm = 0
    for i in range(0, 3):
        _X = np.transpose(X[i])
        _Y = np.transpose(Y[i])
        _B = np.transpose(B)
        norm += np.linalg.norm(A * _X + _B - _Y)
    return norm


# In[5]:


# --------------------- Conjugate Gradient below --------------------

# In[6]:


X = [[1, 2, 3],
     [1, 2, 3],
     [-1, 2, -1]]
Y = [[-1, -3, 1],
     [1, -3, 1],
     [0, 1, 2]]
A = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
B = [1, 1, 1]
A = np.matrix(A)
B = np.matrix(B)
X = np.matrix(X)
Y = np.matrix(Y)
# print(derivateA(X, Y, A, B))
# print(derivateB(X, Y, A, B))
# print(LValue(X, Y, A, B))

# #####  Get the new point by $x_2 = x_1 + \lambda \ S_1$

# In[7]:


L = LValue(X, Y, A, B)
pointOfL = [L]
index = 1
while True:
    directionOfA = -derivateA(X, Y, A, B)
    directionOfB = -derivateB(X, Y, A, B)
    A = A + 0.01 * directionOfA
    B = B + 0.01 * np.transpose(directionOfB)
    newL = LValue(X, Y, A, B)
    pointOfL.append(newL)
    index += 1
    if (L - newL) <= 0.0000000000001:
        break
    else:
        L = newL
x_axis = np.linspace(0, index, index)
y_axis = np.array(pointOfL)
plt.figure(1)
plt.plot(x_axis, y_axis)
plt.xlabel("iterators")
plt.ylabel("values")
plt.show()

# In[8]:


A = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
A = np.matrix(A)
A = np.transpose(A)
X = [[1, 2, 3, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0],
     [0, 0, 0, 1, 2, 3, 0, 0, 0, 0, 1, 0, 0, -5, 0],
     [0, 0, 0, 0, 0, 0, -1, 2, -1, 0, 0, 0, 0, 0, 2]]

X = np.matrix(X)
Y = [[-1, -3, 1],
     [1, -3, 1],
     [0, 1, 2]]
Y = np.matrix(Y)
# print("A Matrix: ", A.shape)
# print("X Matrix: ", X.shape)
# print("Y Matrix: ", Y.shape)


# In[9]:


# 2* X ^ t * (X * A - y)
def derivateFunc(X, A, Y):
    newM = np.zeros((12, 1))
    newM = np.matrix(newM)

    #     for i in range (0, 3):
    #         _Y = np.transpose(Y[i])
    #         newM += 2 * np.transpose(X) * (X * A - _Y)
    return 2 * np.transpose(X) * X * A


# In[10]:


def lossFuc(X, A, Y):
    norm = 0
    #     for i in range (0, 3):
    #         _Y = np.transpose(Y[i])
    #         norm += np.linalg.norm(X*A)
    return np.linalg.norm(X * A)


# In[11]:


def hassenfuc(X):
    return 2 * (np.transpose(X) * X)


# In[12]:


def nabla(X, A, Y, p, Q):
    val = 0
    fx = -derivateFunc(X, A, Y)
    val = (np.transpose(fx) * p) / (np.transpose(p) * Q * p)
    return (np.asarray(val)).flatten()[0]


# In[13]:


def beta(p, Q, r):
    val = (np.transpose(p) * Q * r) / (np.transpose(p) * Q * p)
    return (np.asarray(val)).flatten()[0]


# loss function
lossValue = []
L = lossFuc(X, A, Y)
lossValue.append(L)
# initialize data
p = -derivateFunc(X, A, Y)
Q = hassenfuc(X)
index = 1
while True:
    nab = nabla(X, A, Y, p, Q)
    A = A + nab * p
    newL = lossFuc(X, A, Y)
    lossValue.append(newL)
    index += 1
    if (L - newL) <= 0.001:
        break
    else:
        L = newL
    r = Q * A
    bet = beta(p, Q, r)
    p = -r + bet * p

x_axis = np.linspace(0, index, index)
y_axis = np.array(lossValue)
plt.figure(1)
plt.plot(x_axis, y_axis)
plt.xlabel("iterators")
plt.ylabel("values")
plt.show()
#
