import numpy as np

n = int(input('Please enter a number: '))
arr = np.zeros((n,n))
new_arr = np.zeros((n,n))
for i in range(n):
    for j in range(n):
        arr[i,j] = int(input('({0},{1}): please enter a number: '.format(i+1,j+1)))
        new_arr[j,i] = arr[i,j]

print(new_arr)