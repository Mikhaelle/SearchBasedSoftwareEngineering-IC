import numpy as np
import scipy as sp

c = [50, 40,60]
A = [[-10,-5,-10],[1,1,1],[-1,-1,-1],[-1,0,0]]
b = [-100000,15000,-12000,-5000]
x0_bounds = (0, None)
x1_bounds = (0, None)
x2_bounds = (0, None)

from scipy.optimize import linprog
# Solve the problem by Simplex method in Optimization
res = linprog(c, A_ub=A, b_ub=b,  bounds=(x0_bounds, x1_bounds, x2_bounds), method='simplex', options={"disp": True})
print(res)
