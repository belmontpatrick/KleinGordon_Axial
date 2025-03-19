import numpy as np

#defining grid in time

t0 = 0
tf = 2
delta = t0 - tf
h = 0.001
N = int((tf - t0) / h)
t = np.linspace(t0,tf,N)

