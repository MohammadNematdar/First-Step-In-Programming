import numpy as np

arr = np.zeros((3,3))

for i in range(3):
    for j in range(3):
        arr[i,j] = int(input('({0},{1}): Please enter a number: '.format(i,j)))

print(arr)
print('determinant: ',np.linalg.det(arr))