import numpy as np
#import math
#from scipy import ndimage
import skimage
n = int(input('Please set (n) to build a 2**n,2**n matrix: '))

arr = np.zeros((pow(2,n),pow(2,n)))
#avg_arr = np.zeros((pow(2,n-1),pow(2,n-1)))
print('array shape: ',arr.shape)
#print('array shape: ',avg_arr.shape)

for i in range(pow(2,n)):
    for j in range(pow(2,n)):
        arr[i,j] = int(input('({0},{1}): Please enter a number: '.format(i,j)))



avg_arr = np.mean(arr,axis=1) 
avg_arr = avg_arr.reshape(pow(2,n-1),pow(2,n-1))

print("Original matrix:\n",arr,"\n")
print("Average Pooling From Rows Matrix:\n",avg_arr)