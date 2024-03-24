import numpy as np
n = int(input('please enter a number: '))
arr = np.zeros((n,),dtype=float)

counter = 0
while counter < n:
    R = input('{0}. Please enter a number: '.format(counter + 1))
    arr[counter] = R
    counter += 1

#print(arr[0])
sum = 0
j = 0
c = 0
for i in arr:
    if (j+1)%4 == 0:
        #print(i)
        sum = sum + i
        c = c + 1
    j += 1

print('Miangin adaade mazrabe 4: ',sum/c)



