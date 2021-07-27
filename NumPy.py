"""
What is NumPy.
Ans:-
NumPy is mostly used for the Liner Algebra in python.
And it is used for performing Mathematical and Logical Operations on array.
Provides features for operations on multi-dimensional arrays and matrices in Python.

"""

import numpy as np

# 1D array
a = np.array([1, 2, 3])
print("1D array")
print(a)
print("\n")

# 2D array
b = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array")
print(b)
print("\n")

# Initialize a 5*5 array comprising of all Zeros
c = np.zeros((5, 5))
print("5*5 array with comprising of all Zeros")
print(c)
print("\n")

# Adding 2 Matrices
d = np.array([1, 2, 3])
e = np.array([4, 5, 6])
f = np.sum((d, e), axis=0)
print("Adding 2 Matrices")
print(f)
print("\n")

