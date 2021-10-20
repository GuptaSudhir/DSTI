#!/usr/bin/env python
# coding: utf-8

# In[4]:


import ctypes
import os
import sys
import pygmo as pg
from pygmo import *
import numpy as np
import sys  
sys.path.insert(14, '../cec08/')
import data
from data import rastrigin, f_bias


# In[10]:


import numpy as np
from numba import njit

class Shifted_Rastrigin:
    def __init__(self, dim):
        self.dim = dim
        self.upper = np.zeros([self.dim])
        self.lower = np.zeros([self.dim])
        for i in range(self.dim):
            self.upper[i] = 5
            self.lower[i] = -5
    # No python C++ execution for performance gains
    @njit
    def fitness_fast(x,rastrigin,dim):
        F = 0
        for i in range(dim):
            z = x[i]-rastrigin[i]
            F += (np.power(z,2) - 10*np.cos(2*np.pi*z) + 10)
        return F
    def fitness(self, x):
        retval = np.zeros((1,),dtype=float)
        retval[0] = Shifted_Rastrigin.fitness_fast(x,rastrigin,self.dim) +  f_bias[3]
        return retval
    def get_bounds(self):
        return (self.lower,self.upper)
    def get_name(self):
        return "Shifted Rastrigin CEC08"
    def get_extra_info(self):
        return "\tDimensions: " + str(self.dim)

