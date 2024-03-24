import numpy as np

m = int(input('rows: '))
n = int(input('columns: '))

arr = np.zeros((m,n))
for i in range(m):
    for j in range(n):
            arr[i,j] = input('({0},{1}): '.format(i,j))

arr_transpose = np.transpose(arr)
print('array: ',arr)
print('array-transpose: ',arr_transpose)
