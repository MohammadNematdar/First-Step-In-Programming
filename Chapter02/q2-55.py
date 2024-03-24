import numpy as np

n = int(input('Welcome to Pascal\'s Triangle! Please enter the rows: '))
arr = np.zeros((n,2*n+1))
arr[0,n] = 1
for i in range(1,n):
    for j in range(1,2*n):
        arr[i,j] = arr[i-1,j-1] + arr[i-1,j+1]

print(arr)


print('\n removing zeroes: \n')
l2 = []

for i in range(0,n):
    l = []
    for j in range(0,2*n):
        if arr[i,j] != 0:
            if i == i:
                l.append(arr[i,j])
            else:
                l = arr[i,j]
    l2 = l2 + [l]        

for i in l2:
    print(i)
