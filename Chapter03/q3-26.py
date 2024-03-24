import numpy as np
#import math
#from scipy import ndimage
import skimage

m = int(input('Please enter a number(m): '))
n = int(input('Please enter a number(n): '))

arr = np.zeros((m,n))

for i in range(m):
    for j in range(n):
        arr[i,j] = int(input('({0},{1}): Please enter a number: '.format(i,j)))


arr_transpose = np.transpose(arr)

def isSymmetric(array,transpose):
    if np.array_equal(arr,arr_transpose):
        return True
    return False

result = isSymmetric(arr,arr_transpose)
print("Is matrix symmetric: \n ", result)