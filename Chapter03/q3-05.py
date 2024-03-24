import numpy as np
n = int(input('Shape: '))
k = int(input('Shift: '))
arr = np.zeros((n,),dtype=float)

counter = 0
while counter < n:
    R = input('{0}. Please enter a number: '.format(counter + 1))
    arr[counter] = R
    counter += 1

print(arr)
j = 0
new_arr = np.zeros((n,),dtype=float)
for i in arr:
    if j + k < n:
        new_arr[j+k] = i
    else:
        new_arr[(j+k)-n] = i
    j += 1
print(new_arr)




