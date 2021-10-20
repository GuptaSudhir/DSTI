#!/usr/bin/env python
# coding: utf-8

# In[12]:


import ctypes
import os
import sys
import pygmo as pg
from pygmo import *
import numpy as np
import sys  
sys.path.insert(11, '../cec08/')
import data
from data import sphere, f_bias


# In[13]:


import numpy as np
from numba import njit

class Shifted_Sphere:
    def __init__(self, dim):
        self.dim = dim
        self.upper = np.zeros([self.dim])
        self.lower = np.zeros([self.dim])
        for i in range(self.dim):
            self.upper[i] = 100
            self.lower[i] = -100
    # No python C++ execution for performance gains
    @njit
    def fitness_fast(x,sphere,dim):
        retval = 0.0
        for i in range(dim):
            z = x[i]-sphere[i]
            retval += z*z
        return retval
    def fitness(self, x):
        retval = np.zeros((1,),dtype=float)
        retval[0]  = Shifted_Sphere.fitness_fast(x,sphere,self.dim) +  f_bias[0]
        return retval
    def get_bounds(self):
        return (self.lower,self.upper)
    def get_name(self):
        return "Shifted Sphere CEC08"
    def get_extra_info(self):
        return "\tDimensions: " + str(self.dim)

