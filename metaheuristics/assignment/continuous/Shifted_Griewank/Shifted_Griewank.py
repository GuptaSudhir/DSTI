#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import ctypes
import os
import sys
import pygmo as pg
from pygmo import *
import numpy as np
import sys  
sys.path.insert(13, '../cec08/')
import data
from data import griewank, f_bias


# In[ ]:


import numpy as np
from numba import njit

class Shifted_Griewank:
    def __init__(self, dim):
        self.dim = dim
        self.upper = np.zeros([self.dim])
        self.lower = np.zeros([self.dim])
        for i in range(self.dim):
            self.upper[i] = 600
            self.lower[i] = -600
    # No python C++ execution for performance gains
    @njit
    def fitness_fast(x,griewank,dim):
        F1=0
        F2 = 1
        for i in range(dim):
            z = x[i] - griewank[i]
            F1 += np.power(z,2) / 4000 
            F2 *= np.cos(z/np.sqrt(i+1))
        return (F1 - F2 + 1)
    def fitness(self, x):
        retval = np.zeros((1,),dtype=float)
        retval[0] = Shifted_Griewank.fitness_fast(x,griewank,self.dim) + f_bias[4]
        return retval
    def get_bounds(self):
        return (self.lower,self.upper)
    def get_name(self):
        return "Shifted Griewank CEC08"
    def get_extra_info(self):
        return "\tDimensions: " + str(self.dim)

