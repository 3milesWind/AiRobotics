#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt
from sympy import *
from scipy import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#
# ##   Only accept 2D dimension function formal

# In[2]:


"""
   Change Function to do the process
   Only accept 2D dimension function formal
"""


def funcformat():
    x, y = symbols('x y')
    return x ** 2 - x * y + 3 * y ** 2 + 5


# In[3]:


"""
   Do the Derivative for the function
"""


def derivative(element, f):
    derivedFunc = f.diff(element)
    return derivedFunc


# #### Step1: find out the $\triangledown f$

# In[4]:


def findout_derivateF():
    f = funcformat()
    _symbols = ['x', 'y']
    _diffEquation = []
    for symbol in _symbols:
        _diffEquation.append(derivative(symbol, f))
    return _diffEquation


# #### Step1: find out the $-\triangledown f$ and plug into values

# In[5]:


def findout_NegderivateF(diffEquation, Point):
    searchDirection = []
    for _f in diffEquation:
        x = Point[0]
        y = Point[1]
        searchDirection.append(-(_f.subs([('x', x), ('y', y)])))
    return searchDirection


# #####  Get the new point by $x_2 = x_1 + \lambda \ S_1$

# In[6]:


def newPoint(initPoint, seachDirection):
    for i in range(0, 2):
        initPoint[i] = initPoint[i] + 0.3 * seachDirection[i]  # include learning rate
    return initPoint


# #### Function values 

# In[7]:


def funcValue(x, y):
    return x ** 2 - x * y + 3 * y ** 2 + 5


# ## main 

# In[8]:


"""
  Staring point is [2, 2] -> change it if you need 
  iterate 20 times
  
"""
StartPoint = [2, 2]
iterator = 0
funcValue_y = []
funcValue_x = []
descent_x = []
descent_y = []

# In[9]:


x = np.linspace(-1.5, 2, 50)
y = np.linspace(-1.5, 2, 50)
x, y = np.meshgrid(x, y)
plt.contour(x, y, funcValue(x, y), levels=10)


def animate(i):
    # Got the Derivated function
    diffEquation = findout_derivateF();
    # Got the search direction
    seachDirection = findout_NegderivateF(diffEquation, StartPoint)
    descent_x.append(StartPoint[0])
    descent_y.append(StartPoint[1])
    for i in range(0, 2):
        StartPoint[i] = StartPoint[i] + 0.3 * seachDirection[i]
    plt.clf()
    plt.contour(x, y, funcValue(x, y), levels=10)
    plt.plot(descent_x, descent_y)
    plt.scatter(descent_x, descent_y)


animation = FuncAnimation(plt.gcf(), func=animate, frames=np.arange(0, 20, 1), interval=500)
plt.tight_layout()
plt.show()

# In[ ]:
