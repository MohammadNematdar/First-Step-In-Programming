import numpy as np

arr = np.zeros((5,6))

counter = 0
k = 2
l = [2,]

while counter < 30:
    flag = 0
    k += 1
    for i in range(2,k):
        if k%i == 0:
            flag = 1
    if flag == 0:
        l.append(k)
        counter += 1
#print(l)
n = 0
for i in range(5):
    for j in range(6):
        arr[i,j] = l[n]
        n += 1

print('The first 30 primary numbers:\n',arr)
