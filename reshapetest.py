import numpy as np

A = np.array([[1,2,3],[4,5,6]])


B = A.reshape(-1,1)

C = B.reshape(2,3)

print(C)