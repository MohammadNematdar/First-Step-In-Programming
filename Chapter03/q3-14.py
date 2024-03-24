import numpy as np

m  = int(input('rows: '))
n = int(input('columns: '))
arr = np.zeros((m,n))

sum = 0
for i in range(m):
    for j in range(n):
        R = int(input('({0},{1}): '.format(i,j)))
        sum = sum + R
        arr[i,j] = R

print('original array: ',arr)
AVG = sum/(m*n)
new_arr = np.zeros((m,n))
for i in range(m):
    for j in range(n):
        if arr[i,j] > AVG:
            new_arr[i,j] = arr[i,j]/2
        elif arr[i,j] < AVG:
            new_arr[i,j] = arr[i,j]*2
        elif arr[i,j] == AVG:
            new_arr[i,j] = arr[i,j]

print('filtered array: ',new_arr)
