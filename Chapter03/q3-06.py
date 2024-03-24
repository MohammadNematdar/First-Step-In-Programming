import numpy as np
m = int(input('Shape array_m: '))
n = int(input('Shape array_n: '))
arr_m = np.zeros((m,))
arr_n = np.zeros((n,))
arr_mn = np.zeros((m+n,))
j=0
for i in range(m):
    arr_m[i] = input('{0}. enter a number: '.format(i))
    arr_mn[j] = arr_m[i]
    j += 1

for i in range(n):
    arr_n[i] = input('{0}. enter a number: '.format(i))
    arr_mn[j] = arr_n[i]
    j += 1

print('m: ', arr_m)
print('n: ', arr_n)
print('m+n', arr_mn)