import numpy as np

m = int(input('m.please enter a number(k,m)(m,n): '))
k = int(input('k.please enter a number(k,m)(m,n): '))
n = int(input('n.please enter a number(k,m)(m,n): '))

arr_km = np.zeros((k,m))
arr_mn = np.zeros((m,n))

for i in range(k):
    for j in range(m):
            arr_km[i,j] = int(input('({0},{1})please enter a number(k,m): '.format(i,j)))
print('(A(k,m))',arr_km)

for i in range(m):
    for j in range(n):
            arr_mn[i,j] = int(input('({0},{1})please enter a number(m,n): '.format(i,j)))

print(('B(m,n)'),arr_mn)

print('Multiplication of A & B: ', np.dot(arr_km,arr_mn))