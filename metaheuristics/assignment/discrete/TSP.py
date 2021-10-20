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


# In[2]:


import numpy as np
from numba import njit
import tsplib95


class TSP:
    def __init__(self, dim, filename):
        self.dim = dim
        self.upper = np.zeros([self.dim])
        self.lower = np.zeros([self.dim])
        for i in range(self.dim):
            self.upper[i] = 1
            self.lower[i] = 0
        self.problem = tsplib95.load(filename)
        self.cityGraph = self.problem.get_graph()
        print(self.cityGraph)
    def fitness(self, x):
        distance = 0
        indices_arr = np.argsort(x)
#        print(x)
        print(indices_arr)
        for k in range(self.dim-1):
#            print('k:'+ str(k))
            edge = indices_arr[k]+1,indices_arr[k+1]+1 
            weight = self.problem.get_weight(*edge)
            distance = distance + weight
#            print('weight:' + str(weight))
#            print('distance:' + str(distance))
        print('final distance:' + str(distance))
        retval = np.zeros((1,),dtype=float)
        retval[0]  = distance
        return retval
    def get_bounds(self):
        return (self.lower,self.upper)
    def get_name(self):
        return "Travelling Salesman Problem"
    def get_extra_info(self):
        return "\tDimensions: " + str(self.dim)


# In[3]:


import datetime
def evaluate_TSP_Using_Default(dim, filename):
    prob = pg.problem(TSP(dim,filename))
    print(prob) 
    logs = []
    champion = []
    fitness_value = []
    generations = []
    Bestchamp = 0
    uda = sga(gen = 2500, cr = 0.9, eta_c = 1.0, m = 0.02, param_m = 1.0, param_s = 2, crossover = 'exponential', mutation = 'uniform', selection = 'tournament')    
    start_time = datetime.datetime.now()
    for i in range(25):    
        algo = pg.algorithm(uda)
        algo.set_verbosity(100)
        pop = pg.population(prob,100)
        pop = algo.evolve(pop)

        if(pop.get_f()[pop.best_idx()][0] < Bestchamp):
            Bestchamp = pop.get_f()[pop.best_idx()][0]
            logs = algo.extract(type(uda)).get_log()
        champion.append( pop.get_f()[pop.best_idx()][0])
        
    for i in range(len(logs)):
        fitness_value.append(logs[i][2])
        generations.append(logs[i][1])
    
    plt.plot(generations, fitness_value) 
    # naming the x axis 
    plt.xlabel('Function Evals') 
    # naming the y axis 
    plt.ylabel('Fitness Value') 
    plt.show() 
    
    end_time = datetime.datetime.now()
    span = end_time-start_time
    champions = np.sort(champion)
    print("Best minimas of each run:")
    print(champions)
    print(", ".join(["Params:",str(dim) , str(num_gen), str(population_size), str(omega), str(eta1), str(eta2), str(max_vel), "5", "1", "True", "1"]))
    print(" ".join(["Time span:",str(span.total_seconds())]))
    print('Best loss' + str(-(optima-champions[0])))


# In[ ]:


evaluate_TSP_Using_Default(38,'./dj38.tsp')
