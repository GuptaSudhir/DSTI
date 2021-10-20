This repository contains the source code for the S20 metheuristics assignment

# Metaheuristics Assignment
There are 2 discrete optimization problems and 6 continuous problems.
## Continuous optimization problems
There are 6 problems taken from CEC2008. 
### Code structure and explanation
in the folder assignment/continuous we have a main.ipynb notebook and folders with functions names which contains 
- Thinking about what algorithm has been used to solve the optimization problem.
- Parameters choice
- Software used to solve the optimization problems
  - We have used PyGMO python library for optimization algorithms and problem definition. see https://esa.github.io/pygmo/
  - We have used Particle Swarm Optimization as the algorithm to solve all 6 problem.
  - Parallel Architecture of software in python using the PyGMO library. 
  - Code to invoke the algorithm
  - Code definition of the problems in there respective folders as notebook and python files
- Results of the experiments done to solve the problems.
  - Output of all the problems
  - Best minimas
  - Time taken to solve the problem
  - fitness vs FES graph
## Discrete optimization problems
There are 2 discrete optimization problems. They are travelling salesman problem for two countries
- Djibouti with 38 cities and
- Qatar with 194 cities
### Code structure and explanation
Notebook named TSP.ipynb contains the code of TSP problem definition in python using PyGMO library
- Software used to solve optimization problem
  - We have used PyGMO python library for optimization algorithms and problem definition. see https://esa.github.io/pygmo/
  - We have used simple genetic algorithm to solve both the discrete optimization problems.
  - Parallel Architecture of software in python using the PyGMO library. 
  - Code to invoke the algorithm
  - Code definition of the problems
- Results of the experiments done to solve the problems.
  - Output of all the problems
  - Best minimas
  - Time taken to solve the problem
  - fitness vs FES graph

## How to run the software
metaheuristics folder contains a file named environment.yml which can be used to replicate the software environment used for solving the problems. We have used anaconda to create the environment and exported the environment.yml file.
### Hardware used
We have used Macbook pro laptop with 16 GB memory and i9 processor running the Big sur os to solve all these problems
### Continuous Problems
For Continuous problems open the main.ipynb file present in the folder metaheuristics/assignment/continuous. Now run the entire notebook to recreate the outputs of all the 6 problems. It will take around 8-10 seconds each to execute the problems using 50 dimensions and 5-7 minutes each for 500 dimensions. So in all it will take around **40-45 minutes overall to execute all the optimization** problems for both 50 and 500 dimensions. 
### Discrete Problems
For Discrete problems open the TSP.ipynb file present in the folder metaheuristics/assignment/discrete. Now run the entire notebook to recreate the outputs of both the problems.It will take around **6-7 minutes to execute both the problems** and recreate the output.


