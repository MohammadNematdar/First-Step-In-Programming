import numpy as np

a = int(input('please enter a number: '))
b = int(input('please enter the 2nd number: '))
c = int(input('please enter the 3rd number: '))
d = int(input('please enter the 4th number: '))

matrix = np.matrix([[a , b], [c , d]])

for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        if matrix[i,j] % 2 == 0:
            print('i: ', i+1, 'j: ', j+1)
