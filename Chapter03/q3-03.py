import numpy as np
n = int(input('please enter a number: '))
arr = np.zeros((n,),dtype=float)
R = 7
counter = 0
while counter < n:
    arr[counter] = R
    counter += 1
    R += 3

print(arr)






