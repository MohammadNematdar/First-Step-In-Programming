import numpy as np
n = int(input('please enter a number: '))
arr = np.zeros((n,),dtype=float)

counter = 0
while counter < n:
    R = input('{0}. Please enter a number: '.format(counter + 1))
    arr[counter] = R
    counter += 1

#print(arr[0])
j = 0
for i in arr:
    if (j+1)%2 != 0:
        print(i)
    j += 1





