import numpy as np
n = int(input('Shape: '))
m = int(input('m: '))


arr = np.zeros((n,))
for i in range(n):
    arr[i] = input('({0}): '.format(i))


arr_m = np.zeros((n-1,))
count = 0
c = 0
for i in range(n):
    if i == m - 1:
        c += 1
        pass
    else:
        arr_m[count] = arr[c] 
        c += 1
        count += 1

print(arr)
print('array with m section deleted: ',arr_m)