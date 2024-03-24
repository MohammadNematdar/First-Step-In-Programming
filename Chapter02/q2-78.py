import numpy as np
from math import floor
a = float(input('please enter a number: '))
b = float(input('please enter the 2nd number: '))
c = float(input('please enter the 3rd number: '))
d = float(input('please enter the 4th number: '))

matrix = np.matrix([[a , b], [c , d]])

for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        if matrix[i,j] != floor(matrix[i,j]):
            matrix[i,j] = floor(matrix[i,j])
print(matrix)
