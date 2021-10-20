#!/usr/bin/env python
# coding: utf-8

# In[8]:


import ctypes
import os
import sys
import pygmo as pg
from pygmo import *
import numpy as np
import sys  
sys.path.insert(15, '../cec08/')
import data
from data import rosenbrock, f_bias


# In[9]:


import numpy as np
from numba import njit

class Shifted_Rosenbrock:
    def __init__(self, dim):
        self.dim = dim
        self.upper = np.zeros([self.dim])
        self.lower = np.zeros([self.dim])
        for i in range(self.dim):
            self.upper[i] = 100
            self.lower[i] = -100
    # No python C++ execution for performance gains
    @njit
    def fitness_fast(x,rosenbrock,dim):
        F = 0
        for i in range(dim-1):
            z = x[i] - rosenbrock[i] + 1
            z1 = x[i+1] - rosenbrock[i+1] + 1
            zs = z*z
            F += 100*((zs-z1)*(zs-z1)) + (z-1)*(z-1)
        return F
    def fitness(self, x):
        retval = np.zeros((1,),dtype=float)
        retval[0]  = Shifted_Rosenbrock.fitness_fast(x,rosenbrock,self.dim) +  f_bias[2]
        return retval
    def get_bounds(self):
        return (self.lower,self.upper)
    def get_name(self):
        return "Shifted Rosenbrock CEC08"
    def get_extra_info(self):
        return "\tDimensions: " + str(self.dim)

