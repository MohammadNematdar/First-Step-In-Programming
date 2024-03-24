import numpy as np
import skimage
n = int(input('Please set (n) to build a 2**n,2**n matrix: '))

arr = np.zeros((pow(2,n),pow(2,n)))

print('array shape: ',arr.shape)


for i in range(pow(2,n)):
    for j in range(pow(2,n)):
        arr[i,j] = int(input('({0},{1}): Please enter a number: '.format(i,j)))


avg_arr = skimage.measure.block_reduce(arr, (pow(2,n-1),pow(2,n-1)), np.max)

print("Original matrix:\n",arr,"\n")
print("Average Pooling Matrix:\n",avg_arr)