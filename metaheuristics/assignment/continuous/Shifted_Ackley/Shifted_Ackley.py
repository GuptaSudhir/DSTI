#!/usr/bin/env python
# coding: utf-8

# In[1]:


import ctypes
import os
import sys
import pygmo as pg
from pygmo import *
import numpy as np
import sys  
sys.path.insert(12, '../cec08/')
import data
from data import ackley, f_bias


# In[2]:


import numpy as np
from numba import njit

class Shifted_Ackley:
    def __init__(self, dim):
        self.dim = dim
        self.upper = np.zeros([self.dim])
        self.lower = np.zeros([self.dim])
        for i in range(self.dim):
            self.upper[i] = 32
            self.lower[i] = -32
    # No python C++ execution for performance gains
    @njit
    def fitness_fast(x,ackley,dim):
        Sum1 = 0
        Sum2 = 0
        for i in range(dim):
            z = x[i] - ackley[i]
            Sum1 += np.power(z , 2)
            Sum2 += np.cos(2*np.pi*z)
        retval = -20*np.exp(-0.2*np.sqrt(Sum1/dim)) - np.exp(Sum2/dim) + np.exp(1) + 20
        return retval
    def fitness(self, x):
        retval = np.zeros((1,),dtype=float)
        retval[0]  = Shifted_Ackley.fitness_fast(x,ackley,self.dim) +  f_bias[5]
        return retval
    def get_bounds(self):
        return (self.lower,self.upper)
    def get_name(self):
        return "Shifted Ackley CEC08"
    def get_extra_info(self):
        return "\tDimensions: " + str(self.dim)

