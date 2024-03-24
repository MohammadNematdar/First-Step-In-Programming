import numpy as np
#from scipy import ndimage
import skimage
n = int(input('Please set (n) to build a 2**n,2**n matrix: '))

arr = np.zeros((pow(2,n),pow(2,n)))

print('array shape: ',arr.shape)


for i in range(pow(2,n)):
    for j in range(pow(2,n)):
        arr[i,j] = int(input('({0},{1}): Please enter a number: '.format(i,j)))

#result = ndimage.generic_filter(arr, np.nanmean, size=2, mode='nearest', cval=np.NaN)

avg_arr = skimage.measure.block_reduce(arr, (pow(2,n-1),pow(2,n-1)), np.mean)

print("Original matrix:\n",arr,"\n")
print("Average Pooling Matrix:\n",avg_arr)


#ANOTHER WAY!

# Getting shape of matrix
#M, N = arr.shape

# Shape of kernel
#K = 2
#L = 2

# Dividing the image size by kernel size
#MK = M // K
#NL = N // L

# Creating a pool
#res = arr[:MK*K, :NL*L].reshape(MK, K, NL, L).mean(axis=(1, 3))

# Display Result
#print("Result:\n",res)