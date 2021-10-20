#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import ctypes
import os
import sys
import pygmo as pg
from pygmo import *
import numpy as np
import sys  
sys.path.insert(0, '../cec08/')
import data
from data import schwefel, f_bias


# In[2]:


import numpy as np
from numba import njit

class Schwefel_Problem:
    def __init__(self, dim):
        self.dim = dim
        self.upper = np.zeros([self.dim])
        self.lower = np.zeros([self.dim])
        for i in range(self.dim):
            self.upper[i] = 100
            self.lower[i] = -100
    # No python C++ execution for performance gains
    @njit
    def fitness_fast(x,schwefel,dim):
        retval = -1000.0
        for i in range(dim):
            z = x[i]-schwefel[i]
            if z < 0:
                z = -1.0*z
            if retval < z:
                retval = z
        return retval
    def fitness(self, x):
        retval = np.zeros((1,),dtype=float)
        retval[0] = Schwefel_Problem.fitness_fast(x, schwefel,self.dim) +  f_bias[1]
        return retval
    def get_bounds(self):
        return (self.lower,self.upper)
    def get_name(self):
        return "Schwefel Problem CEC08"
    def get_extra_info(self):
        return "\tDimensions: " + str(self.dim)

