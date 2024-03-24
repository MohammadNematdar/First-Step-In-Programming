import numpy as np
arr = np.zeros((20,),dtype=float)

counter = 0
while counter < 20:
    R = input('{0}. Please enter a number: '.format(counter + 1))
    arr[counter] = R
    counter += 1

#print(arr[0])
j = -1
for i in arr:
    print(arr[j])
    j -= 1





