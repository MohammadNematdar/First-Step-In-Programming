import numpy as np

m  = int(input('rows: '))
n = int(input('columns: '))
matrix1 = np.zeros((m,n))
for i in range(m):
    for j in range(n):
        matrix1[i,j] = int(input('1.({0},{1}) Please enter a number: '.format(i+1,j+1)))

matrix2 = np.zeros((m,n))
for i in range(m):
    for j in range(n):
        matrix2[i,j] = int(input('2.({0},{1}) Please enter a number: '.format(i+1,j+1)))

print(matrix1)
print(matrix2)
print('sum: ', matrix1+matrix2)