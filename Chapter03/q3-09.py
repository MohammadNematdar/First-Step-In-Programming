import numpy as np

arr = np.zeros((3,4))
for i in range(3):
    for j in range(4):
            arr[i,j] = int(input('({0},{1}). PLEASE enter a number: '.format(i+1,j+1)))

print(arr)