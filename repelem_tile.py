import numpy as np


def repelem(arr, repeats):
    """
    Replicates MATLAB's repelem behavior for N-dimensional arrays.
    
    Parameters:
        arr (numpy.ndarray): Input array.
        repeats (tuple): Number of repetitions along each axis.
    
    Returns:
        numpy.ndarray: Repeated array.
    """
    for axis, rep in enumerate(repeats):
        arr = np.repeat(arr, rep, axis=axis)
    return arr

# # # Example
# A = np.array([[1, 2], [3, 4]])

# C = np.array([[1,3],[2,5]])

# B = repelem(A, (len(C), len(C)))  # Repeat rows 2 times, columns 3 times
# print(B)

# # # ###tile example:

# D = np.tile(C,(len(A),len(A)))
# print(D)

# print(B*D)



# c = np.array([[1,2],[3,4]])
# d = np.array([[2,1],[4,3]])


###Learning aboud tile

# c_ = np.tile(c, 2 , axis = 0)
# d_ = np.array(d, 2 , axis = 0)

# print('tile = ',c_)
# print('repeat = ', d_)

###testar:

#np.tile ## equivale a repmat
#np.repeat ## equivale a repelem

# a = np.array([1,2],[2,1])

# b = np.array([4,5,6],[1,2,3])

# a_ = np.tile(a,len(b),len(b))
# b_ = np.repeat(b,len(a),len(a))

# print('tile =', a_)
# print('repeat =', b_)

#print(a_ * b_)

# a = np.array([[1,2],[3,4]])
# b = np.array([[5,6],[7,8]])

# a_ = np.tile(a, (len(b),len(b)))
# b_ = repelem(b, (len(b),len(b)))

# # print(a_)
# # print(b_)

# c_ = np.linalg.inv(a_*b_)

# print(c_)